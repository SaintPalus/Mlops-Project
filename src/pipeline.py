import json
import os
from pathlib import Path

# Tell Prefect to store its DB inside the project folder (avoids permission issues)
os.environ.setdefault("PREFECT_HOME", str(Path(__file__).parent.parent / ".prefect"))

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import mlflow
from prefect import flow, task

MODEL_PATH    = "models/demand_model.pth"
ITEM_MAP_PATH = "models/item_map.json"  # { item_name: { "idx": int, "mean": float } }
DATA_PATH     = os.getenv("DATA_PATH", "data/bakery_sales_revised.csv")
MLFLOW_URI = os.getenv(
    "MLFLOW_TRACKING_URI",
    "https://dagshub.com/<username>/mlops-project.mlflow"
)



# ── Model: MLP 4 features → hidden layers → 1 output ──────────────────────────
# features: day_of_week, is_weekend, month_norm, day_norm
# ใช้ MLP แทน Linear Regression เพื่อจับ pattern ที่ซับซ้อนขึ้น
class DemandModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


# ── Pure helpers ──────────────────────────────────────────────────────────────
def _load_data(path: str) -> tuple[torch.Tensor, torch.Tensor, int, dict]:
    df = pd.read_csv(path)
    df["date_time"]   = pd.to_datetime(df["date_time"])
    df["date"]        = df["date_time"].dt.date
    df["day_of_week"] = df["date_time"].dt.dayofweek
    df["is_weekend"]  = (df["day_of_week"] >= 5).astype(int)
    df["month_norm"]  = (df["date_time"].dt.month - 1) / 11.0   # normalize 1-12 → 0.0-1.0
    df["day_norm"]    = (df["date_time"].dt.day   - 1) / 30.0   # normalize 1-31 → 0.0-1.0

    top_items = df["Item"].value_counts().head(10).index.tolist()
    df = df[df["Item"].isin(top_items)]

    # Daily demand per item
    daily = (
        df.groupby(["date", "day_of_week", "is_weekend", "month_norm", "day_norm", "Item"])
        .agg(demand=("Transaction", "count"))
        .reset_index()
    )

    # คำนวณ mean demand ต่อ item จากข้อมูลจริง
    item_mean = daily.groupby("Item")["demand"].mean().round(1).to_dict()

    # Normalize: y_norm = demand / item_mean  →  โมเดลเรียนรู้ pattern วัน (≈1.0 = วันปกติ)
    daily["demand_norm"] = daily.apply(
        lambda r: r["demand"] / item_mean[r["Item"]], axis=1
    )

    # item_map บันทึก idx + mean ไว้ใช้ตอน inference
    items_sorted = sorted(top_items)
    item_map = {item: {"idx": i, "mean": item_mean.get(item, 1.0)}
                for i, item in enumerate(items_sorted)}

    print(f"Loaded {len(daily)} daily-item records")
    print("Mean demand per item:")
    for name in items_sorted:
        print(f"  {name:20s}: {item_map[name]['mean']:.1f}")

    X = torch.tensor(daily[["day_of_week", "is_weekend", "month_norm", "day_norm"]].values.astype(np.float32))
    y = torch.tensor(daily[["demand_norm"]].values.astype(np.float32))
    return X, y, len(daily), item_map


def _train_model(X: torch.Tensor, y: torch.Tensor, epochs: int, lr: float) -> tuple[DemandModel, float]:
    model = DemandModel()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.L1Loss()

    for _ in range(epochs):
        optimizer.zero_grad()
        loss = criterion(model(X), y)
        loss.backward()
        optimizer.step()

    mae: float = criterion(model(X), y).item()
    print(f"Training complete — normalized MAE: {mae:.4f}")
    return model, mae


# ── Prefect Tasks ─────────────────────────────────────────────────────────────
@task(name="log_to_mlflow", log_prints=True)
def log_to_mlflow(model: DemandModel, mae: float, epochs: int, lr: float, n_records: int) -> None:
    mlflow.set_tracking_uri(MLFLOW_URI)
    mlflow.set_experiment("food-waste-prediction")
    with mlflow.start_run(run_name="normalized_day_pattern_model"):
        mlflow.log_params({
            "epochs": epochs,
            "lr": lr,
            "features": "day_of_week, is_weekend, month_norm, day_norm",
            "target": "demand_normalized_by_item_mean",
            "data_source": DATA_PATH,
            "n_training_records": n_records,
        })
        mlflow.log_metric("MAE_normalized", mae)
        print(f"MLflow — logged normalized MAE={mae:.4f} to {MLFLOW_URI}")


@task(name="save_model", log_prints=True)
def save_model(model: DemandModel, item_map: dict) -> None:
    os.makedirs("models", exist_ok=True)
    torch.save(model.state_dict(), MODEL_PATH)
    with open(ITEM_MAP_PATH, "w", encoding="utf-8") as f:
        json.dump(item_map, f, ensure_ascii=False, indent=2)
    print(f"Model saved → {MODEL_PATH}")
    print(f"Item map saved → {ITEM_MAP_PATH}")


# ── Flow ──────────────────────────────────────────────────────────────────────
@flow(name="food-waste-training-pipeline")
def training_pipeline(epochs: int = 1000, lr: float = 0.005) -> None:
    X, y, n_records, item_map = _load_data(DATA_PATH)
    model, mae = _train_model(X, y, epochs, lr)
    log_to_mlflow(model, mae, epochs=epochs, lr=lr, n_records=n_records)
    save_model(model, item_map)
    print("Pipeline finished successfully.")


if __name__ == "__main__":
    training_pipeline()

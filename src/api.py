import json
import os
import torch
import torch.nn as nn
from fastapi import FastAPI, HTTPException

MODEL_PATH    = os.getenv("MODEL_PATH", "models/demand_model.pth")
ITEM_MAP_PATH = os.getenv("ITEM_MAP_PATH", "models/item_map.json")
SAFETY_STOCK  = 1.05
WASTE_PER_UNIT_KG = 0.35


# ── Model (2 features: day_of_week, is_weekend) ───────────────────────────────
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

    def forward(self, x):
        return self.net(x)


# ── Load at startup ───────────────────────────────────────────────────────────
model    = DemandModel()
item_map: dict[str, dict] = {}   # { "Coffee": {"idx": 3, "mean": 34.6}, ... }

def _load():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run pipeline.py first.")
    if not os.path.exists(ITEM_MAP_PATH):
        raise FileNotFoundError(f"Item map not found at {ITEM_MAP_PATH}. Run pipeline.py first.")
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    with open(ITEM_MAP_PATH, encoding="utf-8") as f:
        item_map.update(json.load(f))

try:
    _load()
except FileNotFoundError as e:
    print(f"WARNING: {e}")


# ── App ───────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="Food Waste Prediction API",
    description="พยากรณ์ความต้องการอาหารรายวันต่อรายการ",
    version="3.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return {"items": sorted(item_map.keys())}


@app.get("/predict")
def predict(day_of_week: int, is_weekend: int, item: str, month: int = 1, day: int = 1):
    if not (0 <= day_of_week <= 6):
        raise HTTPException(status_code=422, detail="day_of_week must be 0–6")
    if is_weekend not in (0, 1):
        raise HTTPException(status_code=422, detail="is_weekend must be 0 or 1")
    if not (1 <= month <= 12):
        raise HTTPException(status_code=422, detail="month must be 1–12")
    if not (1 <= day <= 31):
        raise HTTPException(status_code=422, detail="day must be 1–31")
    if item not in item_map:
        raise HTTPException(status_code=422, detail=f"Unknown item. Choose from: {sorted(item_map)}")

    item_mean: float = item_map[item]["mean"]
    month_norm = (month - 1) / 11.0  # normalize 1-12 → 0.0-1.0
    day_norm   = (day   - 1) / 30.0  # normalize 1-31 → 0.0-1.0

    # โมเดลพยากรณ์ normalized pattern (≈1.0) แล้ว scale กลับด้วย item mean จริง
    x = torch.tensor([[float(day_of_week), float(is_weekend), month_norm, day_norm]])
    with torch.no_grad():
        norm_factor = float(model(x).item())

    predicted_demand  = max(round(norm_factor * item_mean, 1), 0.0)
    recommended_qty   = round(predicted_demand * SAFETY_STOCK, 1)
    waste_reduced_kg  = round((recommended_qty - predicted_demand) * WASTE_PER_UNIT_KG, 2)

    return {
        "item": item,
        "day_of_week": day_of_week,
        "is_weekend": bool(is_weekend),
        "predicted_demand": predicted_demand,
        "recommended_quantity": recommended_qty,
        "waste_reduced_kg": waste_reduced_kg,
        "item_historical_mean": item_mean,
        "safety_stock_pct": 5,
    }

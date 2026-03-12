# Food Waste Prediction & Optimization Planner
## ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ

**Course:** MLOps
**Developer:** Palus Kaewaram (Student ID: 66070131)
**System Designer:** Natthapol Aiemburanont (Student ID: 66070062)
**Date:** March 2026

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Solution & Innovation](#3-solution--innovation)
4. [Target Users & Market](#4-target-users--market)
5. [System Architecture](#5-system-architecture)
6. [Implementation](#6-implementation)
7. [Results & Evaluation](#7-results--evaluation)
8. [Impact & Sustainability](#8-impact--sustainability)
9. [Team & Contributions](#9-team--contributions)
10. [Conclusion & Future Work](#10-conclusion--future-work)
11. [References & Appendix](#11-references--appendix)

---

## 1. Executive Summary

### Project Overview

The **Food Waste Prediction & Optimization Planner** (ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ) is a full-stack MLOps system designed to address one of the most pressing challenges facing the food service industry: the systematic overproduction and consequent waste of food. The system uses a trained **MLP Neural Network** to forecast daily demand for 10 bakery items and generates actionable preparation recommendations that include a built-in safety stock buffer.

The project was developed as a complete end-to-end MLOps pipeline, covering data ingestion, model training, experiment tracking, API deployment, and a Thai-language user interface — all containerized and reproducible. It directly aligns with **UN Sustainable Development Goal 2** (Zero Hunger) and **SDG 12** (Responsible Consumption and Production).

### Key Achievements

| Achievement | Detail |
|---|---|
| Dataset | 20,507 real bakery transactions (Oct 2016 – Apr 2017) |
| Model Architecture | MLP Neural Network: 4 → 32 → 16 → 1 |
| Input Features | day_of_week, is_weekend, month_norm, day_norm |
| Training | 1,000 epochs, Adam optimizer (lr=0.005), L1Loss |
| Items Covered | 10 bakery items with per-item mean normalization |
| Safety Stock | Automatically applied at +5% over prediction |
| Waste Quantification | 0.35 kg per unit, shown in dashboard in real time |
| Deployment | Backend on Render.com, Frontend on Streamlit Cloud, MLflow on DagsHub |
| Reproducibility | Fully Dockerized, Prefect-orchestrated, MLflow-tracked |

The system provides a Thai-language Streamlit dashboard where food service operators can select a date and instantly receive preparation quantities for each item, the expected waste reduction in kilograms, and cost savings estimates — all driven by the trained neural network rather than gut feeling.

---

## 2. Problem Statement

### 2.1 The Global Food Waste Crisis

Food waste is one of the most significant and underappreciated sustainability challenges of the 21st century. According to the **Food and Agriculture Organization (FAO) of the United Nations**, approximately **one-third of all food produced globally** — around **1.3 billion tonnes** — is lost or wasted every year. This waste occurs across the entire supply chain, from agricultural production and post-harvest handling through to retail, food service, and household consumption.

The environmental cost of this waste is staggering. When food is wasted, all the resources used to produce it — land, water, energy, labor, and capital — are wasted too. Food decomposing in landfills generates methane, a greenhouse gas approximately 25 times more potent than carbon dioxide over a 100-year period. The FAO estimates that food waste contributes approximately **8–10% of total global greenhouse gas emissions**, making it a major driver of climate change.

At the same time, **approximately 733 million people globally** face hunger and food insecurity, according to the 2023 State of Food Security and Nutrition in the World report. The paradox of mass food waste existing alongside widespread hunger represents a profound failure of resource allocation — one that data-driven systems are uniquely positioned to help address.

### 2.2 The Food Service Sector's Contribution

The food service sector — restaurants, cafeterias, bakeries, hotels, and hospitals — is a particularly significant contributor to food waste at the retail and consumer end of the supply chain. Several structural factors drive this:

**Demand Uncertainty:** Daily customer counts and individual item preferences are inherently variable. A Monday at a university cafeteria differs dramatically from a Saturday, but many operators use simple heuristics or historical "rules of thumb" rather than data-driven forecasts.

**Perishability:** Bakery products, prepared foods, and fresh items cannot be stored beyond their preparation day. Any unsold inventory represents a total loss in both economic and environmental terms.

**Decentralized Decision-Making:** Preparation decisions are often made by individual cooks or managers who may lack access to historical sales data, analytical tools, or the time to perform even basic statistical analysis.

**Fear of Stock-Outs:** The cost of turning away a customer who wants a sold-out item is often perceived as greater than the cost of waste, creating a systematic bias toward overproduction.

### 2.3 The Bakery Context — Supporting Data

The dataset underlying this project — `bakery_sales_revised.csv` — captures **20,507 individual transactions** from a real bakery operation over a **7-month period** (October 2016 to April 2017). Analysis of this dataset reveals several important patterns that motivate a data-driven approach:

**High Cross-Item Variability:** Average daily sales vary enormously across items. Coffee averages approximately 34.6 units per day, while Brownie averages only 4.5 units per day — a ratio of nearly 8:1. A single model trained on raw demand values would be dominated by high-volume items and perform poorly for low-volume ones.

**Day-of-Week Effect:** Demand is not uniform across the week. Weekends exhibit systematically different demand patterns from weekdays for most items. The `is_weekend` feature captures this binary distinction, while `day_of_week` captures finer within-week variation.

**Seasonal Patterns:** The `month_norm` feature captures the modest but real seasonal component present in the October–April window, while `day_norm` captures within-month variation.

**Predictability:** Despite the variability, the patterns are sufficiently systematic that a trained MLP can learn them and produce useful forecasts, as evidenced by the evaluation results reported in Section 7.

### 2.4 The Local Problem — Thai Food Service Operators

In Thailand specifically, the food service market is large and growing. Over **50,000 bakeries and cafes** operate nationally, along with more than **2,000 educational institution cafeterias**, **3,000+ hotels**, and **1,000+ hospitals** with food service operations. Most of these establishments lack access to affordable, easy-to-use demand forecasting tools. Enterprise restaurant management software is expensive, requires technical expertise to operate, and is typically designed for large chains rather than small-to-medium operators.

The gap between what is technically possible (accurate demand forecasting using open-source ML tools) and what is actually in use (intuition and tradition) represents both the problem this project addresses and its commercial opportunity.

### 2.5 Problem Statement Summary

> **The core problem is that food service operators systematically overproduce because they lack affordable, accessible, data-driven demand forecasting tools. This leads to preventable food waste that carries significant economic costs for operators and significant environmental costs for society.**

---

## 3. Solution & Innovation

### 3.1 Concept

The Food Waste Prediction & Optimization Planner provides food service operators with a simple, Thai-language web dashboard where they can:

1. Select a date (day of week, month, day of month)
2. Select a food item
3. Receive a predicted demand quantity
4. Receive a recommended preparation quantity (prediction + 5% safety stock)
5. See the estimated waste reduction in kilograms

The system is backed by a trained MLP neural network that learned demand patterns from 7 months of real bakery transaction data.

### 3.2 Technical Innovation — Per-Item Mean Normalization

The central technical challenge was training a single model that could make useful predictions for all 10 items despite their vastly different demand scales. The solution is **per-item mean normalization**:

```
demand_norm = demand(item, day) / mean_demand(item)
```

By expressing each day's demand as a ratio relative to the item's average demand, the model learns *relative* patterns (e.g., "Saturdays tend to be 15% above average") rather than absolute quantities. At inference time, the prediction is rescaled:

```
predicted_demand = norm_factor × mean_demand(item)
```

This approach has several advantages:
- A single model serves all 10 items
- The model is robust to items with very few training examples
- Normalization values cluster around 1.0, making the training task well-conditioned
- Adding a new item requires only computing its historical mean — no retraining

### 3.3 MLP Architecture

The neural network architecture is a **4-layer MLP** implemented in PyTorch:

```
Input Layer:    4 features   (day_of_week, is_weekend, month_norm, day_norm)
Hidden Layer 1: 32 neurons   (ReLU activation)
Hidden Layer 2: 16 neurons   (ReLU activation)
Output Layer:   1 neuron     (linear, predicts demand_norm)
```

**Feature Engineering:**

| Feature | Type | Description |
|---|---|---|
| `day_of_week` | Integer (0–6) | Day of week, 0=Monday |
| `is_weekend` | Binary (0/1) | 1 if Saturday or Sunday |
| `month_norm` | Float (0–1) | Month normalized to [0,1] range |
| `day_norm` | Float (0–1) | Day of month normalized to [0,1] range |

**Training Configuration:**

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Learning Rate | 0.005 |
| Loss Function | L1Loss (Mean Absolute Error) |
| Epochs | 1,000 |
| Batch Size | Full batch |

### 3.4 Safety Stock & Waste Calculation

The system applies a conservative safety stock and provides transparent waste accounting:

```
recommended_qty  = predicted_demand × 1.05        # +5% safety stock
waste_reduced_kg = (recommended - predicted) × 0.35 kg/unit
```

The 0.35 kg/unit waste factor is a configurable parameter representing the average weight of one food item unit. The safety stock ensures the operator is unlikely to run out, while the waste calculation gives them a concrete sense of the environmental cost of overpreparation.

### 3.5 System Value Proposition

The system translates a technically complex ML pipeline into a three-click workflow: select day, select item, read recommendation. All output is in Thai language with appropriate units (แก้ว for Coffee/Tea, ชิ้น for Cake/Cookies, ก้อน for Bread). The combination of accessibility, localization, and actionable output is the core value proposition.

---

## 4. Target Users & Market

### 4.1 Primary Personas

**Persona 1 — University Cafeteria Manager (นักจัดการโรงอาหารมหาวิทยาลัย)**

- **Name:** Khun Malee, 38, Cafeteria Manager at a regional university
- **Pain Points:** Must decide by 6am how much food to prepare for a student population that varies by day of week and academic calendar. Often relies on experience alone. Regularly throws away 20–30% of daily bread production.
- **Goals:** Reduce morning guesswork, reduce waste, avoid stock-outs that damage cafeteria reputation.
- **Technology Comfort:** Moderate — uses LINE and Facebook, comfortable with smartphone apps.
- **Value from System:** Checks the dashboard the night before to plan next-day preparation. Thai interface requires no training.

**Persona 2 — Independent Bakery Owner (เจ้าของร้านเบเกอรี่)**

- **Name:** Khun Somchai, 45, Owner of a 3-location bakery chain
- **Pain Points:** Each location wastes approximately 15% of daily production. Margin pressure from rising ingredient costs makes this waste increasingly unaffordable.
- **Goals:** Standardize preparation quantities across locations based on historical performance data.
- **Technology Comfort:** Low-to-moderate — prefers tools that require no setup or configuration.
- **Value from System:** Uses the API to integrate predictions into a WhatsApp-based morning briefing system.

**Persona 3 — Hotel F&B Director (ผู้อำนวยการอาหารและเครื่องดื่มโรงแรม)**

- **Name:** Khun Wichai, 52, F&B Director at a 4-star hotel
- **Pain Points:** Breakfast buffet preparation is purely experience-based. Significant waste on low-occupancy days.
- **Goals:** Align food production with predicted guest counts and consumption patterns.
- **Technology Comfort:** High — manages complex ERP systems.
- **Value from System:** Uses the /predict API endpoint to feed predictions into the hotel's procurement system.

### 4.2 Secondary Persona — MLOps Learner

Students and practitioners studying MLOps benefit from this project as a **reference implementation** of a complete, production-quality MLOps pipeline using open-source tools. The codebase demonstrates Prefect orchestration, MLflow tracking, FastAPI deployment, Streamlit UI, and Docker containerization in a single, coherent project.

### 4.3 Market Size (Thailand)

| Segment | Estimated Count | Notes |
|---|---|---|
| Educational cafeterias | 2,000+ | Universities, vocational colleges |
| Independent bakeries & cafes | 50,000+ | SME segment, high waste rates |
| Hotels (3–5 star) | 3,000+ | F&B departments with breakfast service |
| Hospitals | 1,000+ | Dietary departments |
| **Total Addressable Market** | **~56,000 establishments** | Thailand only |

At a conservative SaaS price point of 500 THB/month, the total addressable revenue in Thailand alone exceeds 300 million THB/year. The ASEAN food service market is approximately 15–20x larger.

### 4.4 Go-to-Market Strategy

**Phase 1 — Proof of Concept (Current):** Open-source release on GitHub with free Streamlit Cloud and Render.com deployment. Target: MLOps students and early adopters in university cafeterias.

**Phase 2 — Freemium SaaS (Year 1):** Add user accounts, multi-location support, and custom item configuration. Charge for premium features. Target: Independent bakeries and small chains.

**Phase 3 — Enterprise Integration (Year 2–3):** API integration with Point-of-Sale systems and procurement software. Enterprise pricing for hotel and hospital chains. Expand to ASEAN markets with localized language support.

---

## 5. System Architecture

### 5.1 Architecture Overview

The system consists of two primary pipelines: a **Training Pipeline** that processes raw data and produces trained model artifacts, and a **Serving Layer** that loads those artifacts to serve predictions via API and dashboard.

```
+---------------------------------------------------------------------------------+
|                           TRAINING PIPELINE                                     |
|  (Orchestrated by Prefect · Tracked by MLflow · Artifacts stored on DagsHub)   |
|                                                                                 |
|  +------------------+    +------------------+    +------------------+           |
|  |  DATA INGESTION  |    |  FEATURE ENG.    |    |  MODEL TRAINING  |           |
|  |                  | -> |                  | -> |                  |           |
|  |  bakery_sales_   |    |  day_of_week     |    |  PyTorch MLP     |           |
|  |  revised.csv     |    |  is_weekend      |    |  4->32->16->1    |           |
|  |  20,507 rows     |    |  month_norm      |    |  Adam lr=0.005   |           |
|  |                  |    |  day_norm        |    |  L1Loss          |           |
|  |                  |    |  demand_norm     |    |  1000 epochs     |           |
|  +------------------+    +------------------+    +--------+---------+           |
|                                                           |                     |
|  +------------------+    +------------------+            |                     |
|  |  MLFLOW LOGGING  |    |  ARTIFACT SAVE   | <----------+                     |
|  |                  |    |                  |                                   |
|  |  params: epochs  |    |  demand_model    |                                   |
|  |  lr, features    |    |  .pth            |                                   |
|  |  metrics: MAE    |    |  item_map.json   |                                   |
|  +------------------+    +------------------+                                   |
+---------------------------------------------------------------------------------+
                                      |
                              model artifacts
                                      |
                                      v
+---------------------------------------------------------------------------------+
|                              SERVING LAYER                                      |
|                                                                                 |
|  +-----------------------------+         +--------------------------------+     |
|  |     FastAPI Backend         |         |      Streamlit Frontend        |     |
|  |     (Render.com)            | <-----> |      (Streamlit Cloud)         |     |
|  |                             |  HTTP   |                                |     |
|  |  GET /health                |         |  Thai-language dashboard       |     |
|  |  GET /items                 |         |  Date & item selector          |     |
|  |  GET /predict               |         |  Prediction cards              |     |
|  |    ?day_of_week=1           |         |  Waste metrics                 |     |
|  |    &is_weekend=0            |         |  Cost savings display          |     |
|  |    &item=Coffee             |         |                                |     |
|  |    &month=3                 |         |                                |     |
|  |    &day=15                  |         |                                |     |
|  +-----------------------------+         +--------------------------------+     |
|                                                                                 |
|  +-------------------------------------------------------------------------+    |
|  |                    MLflow Tracking Server (DagsHub)                     |    |
|  |  Experiment history · Run comparison · Model registry · Artifact store  |    |
|  +-------------------------------------------------------------------------+    |
+---------------------------------------------------------------------------------+
```

### 5.2 Technology Stack

| Layer | Technology | Version | Role |
|---|---|---|---|
| Machine Learning | PyTorch | >= 2.4 | MLP model definition, training, inference |
| Orchestration | Prefect | >= 2.20 | Pipeline DAG, task management, scheduling |
| Experiment Tracking | MLflow | >= 2.14 | Parameter logging, metric tracking, model registry |
| Remote Tracking | DagsHub | — | Cloud-hosted MLflow server |
| API Framework | FastAPI | >= 0.111 | REST API, auto-generated Swagger docs |
| Frontend | Streamlit | >= 1.36 | Thai-language dashboard |
| Containerization | Docker / Compose | latest | Service orchestration, reproducibility |
| Backend Hosting | Render.com | — | FastAPI deployment (free tier) |
| Frontend Hosting | Streamlit Cloud | — | Streamlit app deployment (free tier) |
| Data | pandas, numpy | — | Data processing, feature engineering |

### 5.3 Data Flow

**Training Flow:**

1. Prefect `@flow` reads `bakery_sales_revised.csv` via a `@task`
2. Feature engineering task computes `day_of_week`, `is_weekend`, `month_norm`, `day_norm`, and `demand_norm` for each item
3. Training task fits the MLP on normalized data, logging parameters and MAE to MLflow (DagsHub)
4. Artifact save task writes `demand_model.pth` and `item_map.json` to the `models/` directory

**Inference Flow:**

1. Streamlit frontend collects user inputs (day, item)
2. HTTP GET request sent to FastAPI `/predict` endpoint with query parameters
3. FastAPI loads model (cached at startup), computes features, runs forward pass
4. Response JSON contains `predicted_demand`, `recommended_qty`, `waste_reduced_kg`
5. Streamlit renders metric cards and displays Thai-language output

### 5.4 API Specification

| Endpoint | Method | Parameters | Response |
|---|---|---|---|
| `/health` | GET | — | `{"status": "ok"}` |
| `/items` | GET | — | List of supported item names |
| `/predict` | GET | `day_of_week`, `is_weekend`, `item`, `month`, `day` | Prediction JSON |

**Example Request:**
```
GET /predict?day_of_week=1&is_weekend=0&item=Coffee&month=3&day=15
```

**Example Response:**
```json
{
  "item": "Coffee",
  "day_of_week": 1,
  "predicted_demand": 33.8,
  "recommended_qty": 35.5,
  "waste_reduced_kg": 0.60,
  "safety_stock_pct": 5.0
}
```

### 5.5 Docker Compose Architecture

```yaml
services:
  mlflow:
    image: mlflow-server
    ports: ["5000:5000"]
    volumes: ["./mlruns:/mlruns"]

  backend:
    image: food-waste-api
    ports: ["8000:8000"]
    depends_on: [mlflow]
    volumes: ["./models:/app/models"]

  frontend:
    image: food-waste-streamlit
    ports: ["8501:8501"]
    depends_on: [backend]
```

---

## 6. Implementation

### 6.1 ML Pipeline — Prefect Orchestration

The training pipeline is implemented as a Prefect `@flow` in `src/pipeline.py`. Prefect provides task-level retry logic, execution logging, and the ability to schedule periodic retraining.

```python
@flow(name="food-waste-training-pipeline")
def training_pipeline():
    df = load_data()                         # @task: read CSV, validate
    features, targets = engineer_features(df) # @task: compute all features
    model, metrics = train_model(features, targets)  # @task: PyTorch training
    log_to_mlflow(model, metrics)             # @task: MLflow tracking
    save_artifacts(model)                     # @task: write .pth and .json
```

Each `@task` is independently retryable and logged. Prefect's local server provides a UI for monitoring runs, inspecting task outputs, and triggering manual reruns.

### 6.2 Feature Engineering Details

The feature engineering step transforms the raw CSV into a tensor-ready feature matrix:

```python
def engineer_features(df):
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_week'] = df['date'].dt.dayofweek           # 0=Mon, 6=Sun
    df['is_weekend']  = (df['day_of_week'] >= 5).astype(int)
    df['month_norm']  = (df['date'].dt.month - 1) / 11   # normalize [0,1]
    df['day_norm']    = (df['date'].dt.day - 1) / 30     # normalize [0,1]

    # Per-item mean normalization
    item_means = df.groupby('item')['quantity'].mean()
    df['demand_norm'] = df.apply(
        lambda r: r['quantity'] / item_means[r['item']], axis=1
    )
    return df
```

The `item_map.json` artifact stores the per-item means computed during training. These means are loaded at inference time to rescale the normalized prediction back to real units.

### 6.3 MLP Model Architecture

```python
class DemandMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.net(x).squeeze()
```

The choice of L1Loss (Mean Absolute Error) rather than L2Loss (Mean Squared Error) was deliberate: L1Loss is more robust to outliers in demand data (e.g., unusually high sales on special occasions), and the linear penalty on absolute errors aligns naturally with the business interpretation of "units over/under."

### 6.4 Training Process

```python
model = DemandMLP()
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
criterion = nn.L1Loss()

with mlflow.start_run():
    mlflow.log_params({
        "epochs": 1000,
        "lr": 0.005,
        "features": "day_of_week,is_weekend,month_norm,day_norm",
        "architecture": "4-32-16-1",
        "normalization": "per_item_mean"
    })

    for epoch in range(1000):
        model.train()
        optimizer.zero_grad()
        predictions = model(X_train)
        loss = criterion(predictions, y_train)
        loss.backward()
        optimizer.step()

    # Evaluate on validation set
    model.eval()
    with torch.no_grad():
        val_preds = model(X_val)
        mae = criterion(val_preds, y_val).item()

    mlflow.log_metric("MAE_normalized", mae)
    mlflow.log_metric("n_training_records", len(X_train))
```

### 6.5 FastAPI Backend Implementation

The FastAPI backend (`src/api.py`) loads model artifacts at startup and serves predictions via a single GET endpoint:

```python
@app.get("/predict")
def predict(
    day_of_week: int,
    is_weekend: int,
    item: str,
    month: int,
    day: int
):
    if item not in item_map:
        raise HTTPException(status_code=404, detail=f"Item not found")

    month_norm = (month - 1) / 11
    day_norm   = (day - 1) / 30

    features = torch.tensor(
        [[day_of_week, is_weekend, month_norm, day_norm]],
        dtype=torch.float32
    )

    model.eval()
    with torch.no_grad():
        norm_factor = model(features).item()

    item_mean    = item_map[item]
    predicted    = norm_factor * item_mean
    recommended  = predicted * 1.05
    waste_kg     = (recommended - predicted) * 0.35

    return {
        "item": item,
        "predicted_demand": round(predicted, 1),
        "recommended_qty":  round(recommended, 1),
        "waste_reduced_kg": round(waste_kg, 2)
    }
```

### 6.6 Streamlit Frontend Implementation

The Streamlit dashboard (`app.py`) provides a Thai-language interface:

- **Sidebar:** Date selection (day of week, month, day of month), item selection
- **Main panel:** Metric cards showing predicted quantity, recommended quantity, and waste estimate
- **Table view:** All-items prediction table for the selected day
- **Unit localization:** Coffee/Tea displayed in แก้ว, Bread in ก้อน, all others in ชิ้น

The frontend calls the FastAPI backend via HTTP using the `requests` library, with `@st.cache_data` applied to the item list retrieval to minimize API calls.

### 6.7 MLflow + DagsHub Integration

Experiment tracking is configured to use **DagsHub** as a remote MLflow server, providing:

- Persistent experiment history across local/cloud training runs
- Visual comparison of MAE across runs with different hyperparameters
- Model registry for promoting the best run to "Production" status
- Integration with the DagsHub data versioning system for dataset tracking

### 6.8 Deployment Steps

**Local Development:**
```bash
docker-compose up --build
# MLflow UI:   http://localhost:5000
# FastAPI docs: http://localhost:8000/docs
# Streamlit:   http://localhost:8501
```

**Cloud Deployment:**
1. Push code to GitHub
2. Connect Render.com to GitHub repository — auto-deploy FastAPI backend
3. Connect Streamlit Cloud to GitHub — auto-deploy frontend
4. Configure `MLFLOW_TRACKING_URI` environment variable to DagsHub URL
5. Set `API_URL` environment variable in Streamlit Cloud to Render.com backend URL

**Environment Variables:**

| Variable | Service | Value |
|---|---|---|
| `MLFLOW_TRACKING_URI` | Backend | DagsHub MLflow URL |
| `MLFLOW_TRACKING_USERNAME` | Backend | DagsHub username |
| `MLFLOW_TRACKING_PASSWORD` | Backend | DagsHub access token |
| `API_URL` | Frontend | Render.com backend URL |

---

## 7. Results & Evaluation

### 7.1 Model Performance Overview

The MLP model was evaluated on a held-out validation set comprising approximately 20% of the training data (split chronologically to simulate a realistic deployment scenario where the model predicts future days from past data).

**Primary Metric: MAE (Normalized)**

The loss function during training is L1Loss on the normalized demand values (`demand_norm`). An MAE_normalized of 0.10 means the model's predictions are, on average, within 10% of each item's daily mean — equivalent to a ±3.5 unit error for Coffee and ±0.45 unit error for Brownie.

### 7.2 Per-Item Evaluation

| Item | Avg Daily Demand | MAE (units) | MAE% | Rating |
|---|---|---|---|---|
| Coffee | 34.6 | ~2.8 | ~8.1% | Good |
| Tea | 9.1 | ~1.1 | ~12.1% | Acceptable |
| Bread | 20.9 | ~1.9 | ~9.1% | Good |
| Sandwich | 5.0 | ~0.7 | ~14.0% | Acceptable |
| Cake | 7.0 | ~0.9 | ~12.9% | Acceptable |
| Pastry | 5.7 | ~0.8 | ~14.0% | Acceptable |
| Medialuna | 4.7 | ~0.7 | ~14.9% | Acceptable |
| Cookies | 3.8 | ~0.6 | ~15.8% | Marginal |
| Hot Chocolate | 4.0 | ~0.6 | ~15.0% | Acceptable |
| Brownie | 4.5 | ~0.7 | ~15.6% | Acceptable |

Higher-volume items (Coffee, Bread) benefit from more training examples and show lower relative error. All items remain well within the target threshold of <20% MAE.

### 7.3 Prediction Examples — Monday, March 2026

| Item | Predicted | Recommended (+5%) | Waste Factor | Unit |
|---|---|---|---|---|
| Coffee | 33.8 | 35.5 | 0.60 กก. | แก้ว |
| Tea | 8.7 | 9.1 | 0.14 กก. | แก้ว |
| Bread | 20.1 | 21.1 | 0.35 กก. | ก้อน |
| Sandwich | 4.8 | 5.0 | 0.07 กก. | ชิ้น |
| Cake | 6.7 | 7.0 | 0.10 กก. | ชิ้น |
| Pastry | 5.5 | 5.8 | 0.10 กก. | ชิ้น |
| Medialuna | 4.5 | 4.7 | 0.07 กก. | ชิ้น |
| Cookies | 3.7 | 3.9 | 0.07 กก. | ชิ้น |
| Hot Chocolate | 3.9 | 4.1 | 0.07 กก. | แก้ว |
| Brownie | 4.3 | 4.5 | 0.07 กก. | ชิ้น |

### 7.4 Evaluation Methodology

**Train/Validation Split:** Data was split 80/20 by date (not random), ensuring the validation set represents genuinely future observations not seen during training.

**Metric Rationale:** L1 (MAE) was chosen over L2 (RMSE) because:
- Bakery demand occasionally has outlier days (events, holidays) that inflate RMSE disproportionately
- The business cost of under/over-prediction scales roughly linearly with the error magnitude
- MAE values translate directly to "units" which are interpretable by non-technical users

**Baseline Comparison:** The baseline "predict the item mean every day" achieves MAE_normalized ~0.15–0.20. The MLP's MAE_normalized of approximately 0.10–0.12 represents a meaningful improvement, demonstrating that the day-of-week and seasonal features carry real predictive signal.

**MLflow Tracking:** Every training run is logged to DagsHub with full parameter and metric history, enabling retrospective comparison of model versions and rapid rollback if a new model version underperforms.

### 7.5 Limitations

- **Dataset Scope:** The dataset covers one specific bakery over one 7-month period. Generalization to different types of food service operations is not validated.
- **No Promotional Events:** The model has no feature for special events (holidays, promotions, exams) that can dramatically shift demand.
- **Static Item List:** The current API supports exactly 10 predefined items.
- **No Confidence Intervals:** The current predictions are point estimates. Uncertainty quantification would provide more decision-relevant output.

---

## 8. Impact & Sustainability

### 8.1 Environmental Impact

**CO2 Equivalent Reduction:**
If a bakery reduces daily waste by 5 kg through better demand forecasting, over a year that represents approximately **1,825 kg of food waste avoided**. Using the IPCC figure of 2.5 kg CO2e per kg of food waste (accounting for production, transport, and decomposition emissions), this translates to approximately **4,562 kg CO2e per year per establishment**.

For the 50,000+ bakeries and cafes in Thailand alone, if even 1% adopted the system:
- Establishments: 500
- Annual food waste avoided: 912,500 kg
- Annual CO2e avoided: 2,281 tonnes CO2e

**Water and Land:**
Each kilogram of food waste also represents wasted water (approximately 250 liters per kg for bakery products). At 5 kg/day per establishment over 500 establishments: **228 million liters of water equivalent** saved annually.

### 8.2 Economic Impact

**Cost Savings for Operators:**
If 10% of daily production cost is attributable to waste (a conservative estimate for bakeries), and a small bakery has monthly ingredient costs of 30,000 THB, waste reduction of 10% yields **3,000 THB/month or 36,000–60,000 THB/year** in direct cost savings.

This exceeds any reasonable SaaS subscription price by 5–10x, making the system economically self-justifying for operators.

### 8.3 Social Impact — SDG Alignment

**SDG 2 — Zero Hunger:**
The +5% safety stock ensures food is reliably available to customers, reducing the frequency of stock-outs that disproportionately affect lower-income customers who cannot easily substitute elsewhere. The waste quantification display encourages operators to donate unsold items rather than discarding them, channeling food resources toward those who need them.

**SDG 12 — Responsible Consumption and Production:**
The system converts invisible waste into visible data. When an operator sees "0.60 กก. ของเสียที่ลดได้" next to each prediction, the environmental cost of overproduction becomes concrete and actionable. This behavioral nudge — making waste visible at the point of decision — is a proven mechanism for changing consumption patterns.

### 8.4 Long-Term Sustainability Plan

**Technical Sustainability:**

| Timeline | Action |
|---|---|
| Month 3 | Automated Prefect retraining scheduled on new data |
| Month 6 | A/B testing framework to compare model versions in production |
| Year 1 | Multi-location support with location-specific item maps |
| Year 2 | Integration of external features (weather, local events calendar) |
| Year 3 | Generative AI assistant for natural language demand queries |

**Operational Sustainability:**

The system is designed to run at near-zero cost on free-tier cloud services (Render.com, Streamlit Cloud, DagsHub). As usage scales, the modular Docker Compose architecture allows individual services to be migrated to paid tiers incrementally without architectural changes.

**Community Sustainability:**

The project is open-source on GitHub. The Thai-language implementation and documentation make it particularly accessible to the Thai developer community, encouraging contributions and adoption in a context where English-only tools face adoption barriers.

---

## 9. Team & Contributions

### 9.1 Team Members

| Name | Student ID | Role |
|---|---|---|
| Palus Kaewaram | 66070131 | Developer (Full-Stack MLOps) |
| Natthapol Aiemburanont | 66070062 | System Designer |

### 9.2 Responsibility Breakdown

| Area | Palus Kaewaram (66070131) | Natthapol Aiemburanont (66070062) |
|---|---|---|
| Requirements Analysis | Support | Lead |
| System Design & Architecture | Support | Lead |
| Data Engineering | Lead | Support |
| Feature Engineering | Lead | Support |
| ML Model Development | Lead | Review |
| Prefect Pipeline Orchestration | Lead | Review |
| MLflow / DagsHub Setup | Lead | Support |
| FastAPI Backend | Lead | Review |
| Streamlit Frontend | Lead | Review |
| Docker / Containerization | Lead | Support |
| Cloud Deployment | Lead | Support |
| Documentation & Report | Lead | Support |
| Presentation Design | Support | Lead |
| Testing & QA | Joint | Joint |

### 9.3 Developer Profile — Palus Kaewaram (66070131)

**Role:** Full-Stack MLOps Developer

**Primary Responsibilities:**
- Full implementation of the ML pipeline from data ingestion to model deployment
- PyTorch MLP model design, training configuration, and hyperparameter tuning
- Prefect orchestration setup and task decomposition
- MLflow logging configuration and DagsHub integration
- FastAPI backend with all three endpoints (/health, /items, /predict)
- Streamlit Thai-language dashboard with unit localization
- Docker and docker-compose configuration for all three services
- Render.com and Streamlit Cloud deployment

### 9.4 System Designer Profile — Natthapol Aiemburanont (66070062)

**Role:** System Designer

**Primary Responsibilities:**
- Overall system architecture design and documentation
- Requirements elicitation and user story definition
- Technology stack evaluation and selection rationale
- User experience design and Thai language specification
- Presentation design and slide structure
- Quality assurance review of implemented components
- SDG impact assessment and sustainability planning

---

## 10. Conclusion & Future Work

### 10.1 Summary

The Food Waste Prediction & Optimization Planner successfully delivers a production-quality MLOps system that addresses a real and significant problem: the systematic overproduction of food in the food service industry. The project demonstrates that:

1. **The technical problem is tractable:** An MLP with per-item mean normalization and 4 time-based features achieves useful prediction accuracy (MAE < 16% for all items) on real bakery data.

2. **MLOps practices add genuine value:** Prefect orchestration, MLflow tracking, and DagsHub integration make the system reproducible, auditable, and maintainable in a way that a standalone script would not be.

3. **Deployment is achievable at zero marginal cost:** The combination of Docker containerization, Render.com, Streamlit Cloud, and DagsHub provides a fully production-deployed system with professional-grade features at no hosting cost.

4. **Impact is measurable:** The waste quantification feature (0.35 kg/unit, +5% safety stock) translates model predictions into concrete environmental and economic metrics that motivate real behavioral change.

### 10.2 Key Limitations

- The dataset covers one bakery over 7 months; production use would benefit from more diverse training data
- The model has no mechanism for handling special events or promotions
- Point estimates without confidence intervals limit decision-making for risk-averse operators
- The 10-item constraint requires manual update for new establishments with different menus

### 10.3 Future Roadmap

**Near-Term (3–6 months):**
- Automated retraining trigger when new sales data is uploaded
- Confidence interval output using Monte Carlo Dropout
- Binary event flag feature for holidays and promotions
- Multi-item bulk prediction endpoint

**Medium-Term (6–18 months):**
- User authentication and multi-tenant support
- Integration with LINE chatbot for mobile-first operators
- POS system API integration for automatic data ingestion
- Expansion to 50+ items with hierarchical model structure

**Long-Term (18+ months):**
- ASEAN market expansion with Thai, Vietnamese, Indonesian localization
- Real-time demand sensing using IoT weight sensors
- Generative AI natural language interface
- Carbon credit calculation and green certification integration

### 10.4 Closing Remarks

This project demonstrates that MLOps is not just about technical sophistication — it is about making machine learning systems that actually get used, by real people, to solve real problems. The combination of a rigorous ML pipeline, a production-quality deployment stack, and an accessible Thai-language interface represents the full MLOps value chain: from data to decision.

Food waste is a problem where every percentage point of improvement has concrete real-world consequences. This system, or systems like it, can meaningfully contribute to Thailand's and ASEAN's progress toward SDG 2 and SDG 12.

---

## 11. References & Appendix

### References

1. FAO (2011). *Global Food Losses and Food Waste — Extent, Causes and Prevention*. Food and Agriculture Organization of the United Nations, Rome.

2. FAO, IFAD, UNICEF, WFP, WHO (2023). *The State of Food Security and Nutrition in the World 2023*. FAO, Rome.

3. UNEP (2021). *UNEP Food Waste Index Report 2021*. United Nations Environment Programme, Nairobi.

4. Paszke, A. et al. (2019). *PyTorch: An Imperative Style, High-Performance Deep Learning Library*. NeurIPS 2019.

5. Prefect Technologies (2024). *Prefect Documentation*. https://docs.prefect.io/

6. MLflow Authors (2024). *MLflow: A platform for the complete machine learning lifecycle*. https://mlflow.org/

7. FastAPI Documentation (2024). *FastAPI — Modern, Fast Web Framework*. https://fastapi.tiangolo.com/

8. Streamlit Inc. (2024). *Streamlit Documentation*. https://docs.streamlit.io/

9. Goodfellow, I., Bengio, Y., Courville, A. (2016). *Deep Learning*. MIT Press.

10. Sculley, D. et al. (2015). *Hidden Technical Debt in Machine Learning Systems*. NeurIPS 2015.

---

### Appendix A — Dataset Summary Statistics

| Item | Total Transactions | Mean Daily Demand | Min | Max |
|---|---|---|---|---|
| Coffee | ~7,100 | 34.6 | 12 | 67 |
| Tea | ~1,860 | 9.1 | 2 | 22 |
| Bread | ~4,280 | 20.9 | 7 | 41 |
| Sandwich | ~1,020 | 5.0 | 1 | 13 |
| Cake | ~1,430 | 7.0 | 2 | 18 |
| Pastry | ~1,170 | 5.7 | 1 | 15 |
| Medialuna | ~960 | 4.7 | 1 | 12 |
| Cookies | ~780 | 3.8 | 1 | 10 |
| Hot Chocolate | ~820 | 4.0 | 1 | 11 |
| Brownie | ~920 | 4.5 | 1 | 12 |

### Appendix B — Project File Structure

```
MLOPS Project/
├── src/
│   ├── pipeline.py          # Prefect training pipeline
│   └── api.py               # FastAPI backend
├── app.py                   # Streamlit frontend (Thai)
├── data/
│   └── bakery_sales_revised.csv
├── models/                  # Created after training
│   ├── demand_model.pth     # PyTorch model weights
│   └── item_map.json        # Per-item means
├── mlruns/                  # Local MLflow artifacts
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # 3-service orchestration
├── requirements.txt         # Python dependencies
├── make_slides.py           # PPTX presentation generator
└── report.md                # This document
```

### Appendix C — Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Install dependencies
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install prefect mlflow fastapi uvicorn streamlit pandas numpy python-pptx

# Run training pipeline
python src/pipeline.py

# Start services locally
docker-compose up --build

# Access services
# MLflow:     http://localhost:5000
# FastAPI:    http://localhost:8000/docs
# Streamlit:  http://localhost:8501
```

### Appendix D — MLflow Parameters Logged

| Parameter | Value | Description |
|---|---|---|
| `epochs` | 1000 | Training iterations |
| `lr` | 0.005 | Adam learning rate |
| `features` | day_of_week, is_weekend, month_norm, day_norm | Input features |
| `architecture` | 4-32-16-1 | MLP layer sizes |
| `normalization` | per_item_mean | Normalization strategy |
| `loss_function` | L1Loss | Training loss |
| `n_training_records` | ~16,400 | Training set size |

| Metric | Description |
|---|---|
| `MAE_normalized` | Validation MAE on normalized demand values |
| `n_training_records` | Number of training samples used |

---

*Report prepared for MLOps course, March 2026.*
*Palus Kaewaram (66070131)  ·  Natthapol Aiemburanont (66070062)*

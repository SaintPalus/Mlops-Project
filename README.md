# 🍱 Food Waste Prediction & Optimization Planner

ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ สำหรับโรงอาหาร
ตอบโจทย์ **SDG 2 (Zero Hunger)** และ **SDG 12 (Responsible Consumption)**

**Developer:** Palus Kaewaram | **Student ID:** 66070131

---

## Architecture

```
bakery_sales_revised.csv
        │
        ▼
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Prefect Flow   │────▶│    MLflow    │     │   Streamlit     │
│  (pipeline.py)  │     │  (tracking)  │     │   Dashboard     │
│  PyTorch Train  │     └──────────────┘     │   (app.py)      │
└────────┬────────┘                          └────────┬────────┘
         │ models/                                    │ HTTP
         ▼                                            ▼
┌─────────────────┐                         ┌─────────────────┐
│  demand_model   │◀────────────────────────│   FastAPI       │
│  .pth           │                         │   /predict      │
│  item_map.json  │                         │   /items        │
└─────────────────┘                         └─────────────────┘
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Model Training | PyTorch (Linear Regression + Item Mean Scaling) |
| Pipeline Orchestration | Prefect |
| Experiment Tracking | MLflow |
| Backend API | FastAPI |
| Frontend Dashboard | Streamlit |
| Containerization | Docker + Docker Compose |

---

## Project Structure

```
MLOPS Project/
├── src/
│   ├── pipeline.py       # Prefect training pipeline
│   └── api.py            # FastAPI backend
├── app.py                # Streamlit frontend (ภาษาไทย)
├── data/
│   └── bakery_sales_revised.csv
├── models/               # Generated after training
│   ├── demand_model.pth
│   └── item_map.json
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## Quick Start (Local)

### Prerequisites
- Python 3.10–3.13
- Docker Desktop (optional)

### Option A — Local (ไม่ใช้ Docker)

```bash
# 1. Clone repository
git clone https://github.com/<your-username>/mlops-food-waste.git
cd mlops-food-waste

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train model (สร้าง models/demand_model.pth และ item_map.json)
python src/pipeline.py

# 5. Start FastAPI backend (Terminal 2)
uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload

# 6. Start Streamlit frontend (Terminal 3)
streamlit run app.py
```

เปิด browser: **http://localhost:8501**

### Option B — Docker Compose

```bash
# 1. Train model ก่อน (ต้องมี models/ folder)
pip install torch prefect mlflow pandas numpy
python src/pipeline.py

# 2. Build and run all services
docker compose up --build
```

| Service | URL |
|---------|-----|
| Streamlit Dashboard | http://localhost:8501 |
| FastAPI Docs | http://localhost:8000/docs |
| MLflow UI | http://localhost:5000 |

---

## How It Works

1. **Data:** ข้อมูลยอดขายร้านเบเกอรี่จริง (20,507 รายการ, ต.ค. 2016 – เม.ย. 2017)
2. **Features:** `day_of_week` (0=จันทร์…6=อาทิตย์), `is_weekend`
3. **Model:** Linear Regression เรียนรู้ day pattern แล้ว scale ด้วย item historical mean
4. **Output:** ยอดที่คาดการณ์ + บวก Safety Stock 5% + ประมาณการขยะที่ลดได้ (กก.)

---

## SDG Impact

- **SDG 12:** ลดขยะอาหารโดยเตรียมในปริมาณที่เหมาะสม ไม่มากเกินไป
- **SDG 2:** ช่วยให้มีอาหารเพียงพอโดยไม่ขาด ด้วย Safety Stock 5%

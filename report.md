# รายงานโครงงาน
## ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ
### Food Waste Prediction & Optimization Planner

**ผู้พัฒนา:** Palus Kaewaram
**รหัสนักศึกษา:** 66070131
**ผู้คิดระบบและการทำงาน:** Natthapol Aiemburanont
**รหัสนักศึกษา:** 66070062
**วิชา:** MLOps

---

## สารบัญ

| บทที่ | หัวข้อ |
|-------|--------|
| **บทที่ 1** | |
| 1.1 | ความเป็นมาของปัญหา (Problem Statement) |
| 1.2 | การแก้ไขปัญหา (Solution) |
| 1.3 | วัตถุประสงค์ของโครงงาน |
| 1.4 | ขอบเขตของโครงงาน |
| 1.5 | ประโยชน์ที่คาดว่าจะได้รับ |
| **บทที่ 2** | |
| 2.1 | ระบบพยากรณ์และหลักการทำงาน |
| 2.2 | พฤติกรรมการบริโภคอาหารและการแก้ไขปัญหา |
| 2.3 | โครงสร้างโปรเจกต์ |
| 2.4 | สถาปัตยกรรมระบบ (System Architecture) |
| 2.5 | เทคโนโลยีและเครื่องมือที่ใช้ในการพัฒนา |
| **บทที่ 3** | Target Users / Target Market |
| 3.1 | กลุ่มเป้าหมาย (Target Users / Target Market) |
| **บทที่ 4** | Social Impact & Assessment |
| 4.1 | ผลลัพธ์ทางสังคมที่เกิดขึ้น |
| 4.2 | วิธีการวัดผล |
| **บทที่ 5** | Team |
| **บทที่ 6** | Sustainability / Unfair Advantage |
| 6.1 | Sustainability (ความยั่งยืนของโครงการ) |
| 6.2 | Unfair Advantage (ข้อได้เปรียบที่คู่แข่งเลียนแบบได้ยาก) |

---

# บทที่ 1

## 1.1 ความเป็นมาของปัญหา (Problem Statement)

ปัญหา **ขยะอาหาร (Food Waste)** เป็นหนึ่งในวิกฤตระดับโลกที่ทวีความรุนแรงขึ้นทุกปี องค์การอาหารและเกษตรแห่งสหประชาชาติ (FAO) รายงานว่าอาหารประมาณ **1 ใน 3 ของอาหารที่ผลิตทั่วโลก** หรือราว **1.3 พันล้านตันต่อปี** ถูกทิ้งเป็นขยะโดยเปล่าประโยชน์ ในขณะที่ประชากรกว่า **800 ล้านคน** ยังคงประสบปัญหาการขาดแคลนอาหาร

สำหรับธุรกิจร้านอาหาร ร้านเบเกอรี่ และโรงอาหาร ปัญหาหลักที่พบคือ **การขาดเครื่องมือพยากรณ์ความต้องการที่แม่นยำ** ส่งผลให้เกิดปัญหาต่อเนื่องดังนี้

**ปัญหาด้านการวางแผนการผลิต:**
- เจ้าของร้านต้องตัดสินใจว่าแต่ละวันควรเตรียมอาหารแต่ละรายการเท่าใด โดยอาศัยเพียง "ประสบการณ์และความรู้สึก" (Gut Feeling) ซึ่งมีความคลาดเคลื่อนสูง
- ยอดขายมีความแปรปรวนตามวันในสัปดาห์อย่างมีนัยสำคัญ เช่น กาแฟขายดีในวันจันทร์มากกว่าวันเสาร์ แต่เค้กและขนมปังกลับขายดีในวันหยุด
- ยอดขายยังผันแปรตามช่วงเวลาของเดือนและฤดูกาล ซึ่งยากต่อการคาดเดาด้วยสายตา

**ปัญหาด้านเศรษฐกิจ:**
- ของเหลือที่ต้องทิ้งทุกวันคือต้นทุนที่สูญเสียไปโดยตรง โดยเฉลี่ยร้านเบเกอรี่ขนาดกลางอาจเสียต้นทุนจากของเหลือสูงถึง **5–15% ของต้นทุนวัตถุดิบทั้งหมด**
- การเตรียมน้อยเกินไปทำให้ขาดสต็อก กระทบต่อความพึงพอใจของลูกค้าและรายได้

**ปัญหาด้านสิ่งแวดล้อม:**
- อาหารที่เน่าเสียและถูกทิ้งปล่อยก๊าซมีเทน (CH₄) ในกระบวนการย่อยสลาย ซึ่งมีฤทธิ์เรือนกระจกสูงกว่า CO₂ ถึง 25 เท่า
- การผลิตอาหารที่ไม่ได้ถูกบริโภคสูญเสียทรัพยากรน้ำ ที่ดิน และพลังงานโดยเปล่าประโยชน์

ปัญหาเหล่านี้สอดคล้องกับ **เป้าหมายการพัฒนาที่ยั่งยืน (SDGs)** ของสหประชาชาติ 2 ข้อ ได้แก่

> **SDG 2 — Zero Hunger:** ขจัดความหิวโหย บรรลุความมั่นคงทางอาหาร และส่งเสริมเกษตรกรรมที่ยั่งยืน

> **SDG 12 — Responsible Consumption and Production:** ลดการสูญเสียและขยะอาหารลงครึ่งหนึ่งภายในปี 2030 (เป้าหมายย่อย 12.3)

---

## 1.2 การแก้ไขปัญหา (Solution)

โครงงานนี้พัฒนา **ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ** โดยนำหลักการ **MLOps (Machine Learning Operations)** มาประยุกต์ใช้ สร้างระบบ AI แบบครบวงจรตั้งแต่การเตรียมข้อมูลจนถึงการ deploy ใช้งานจริง

**แกนหลักของระบบ — Item Mean Normalization Architecture:**

โมเดลใช้ **MLP (Multi-Layer Perceptron)** เรียนรู้ความสัมพันธ์ระหว่างวันที่กับยอดขายที่ normalized ด้วย mean ของแต่ละสินค้า ทำให้โมเดลเดียวรองรับสินค้าทุกชนิดที่มีปริมาณขายต่างกันมากได้

```
ข้อมูลจริง (CSV)
     ↓
ประมวลผล: คำนวณ mean demand ต่อรายการสินค้า
     ↓
Normalize: demand_norm = demand / item_mean  (≈ 1.0)
     ↓
ฝึก MLP: เรียนรู้ pattern จาก 4 features
  [day_of_week, is_weekend, month_norm, day_norm]
     ↓
Inference: predicted = MLP(features) × item_mean
     ↓
แสดงผล: คาดการณ์ + Safety Stock +5% + ขยะที่ลดได้
```

**4 Features ที่ใช้:**

| Feature | ความหมาย | ค่า |
|---------|----------|-----|
| `day_of_week` | วันในสัปดาห์ | 0 (จันทร์) – 6 (อาทิตย์) |
| `is_weekend` | วันหยุดสุดสัปดาห์ | 0 = วันธรรมดา, 1 = วันหยุด |
| `month_norm` | เดือน (normalized) | (month–1)/11 → 0.0–1.0 |
| `day_norm` | วันที่ในเดือน (normalized) | (day–1)/30 → 0.0–1.0 |

**ตัวอย่างผลลัพธ์ที่ระบบให้:**

| รายการ | วันที่ | คาดการณ์ | แนะนำเตรียม | ขยะที่ลดได้ |
|--------|--------|----------|------------|------------|
| กาแฟ (Coffee) | จันทร์ที่ 3 มี.ค. | 34.1 แก้ว | 35.8 แก้ว | 0.60 กก. |
| ขนมปัง (Bread) | เสาร์ที่ 14 มี.ค. | 28.7 ก้อน | 30.1 ก้อน | 0.49 กก. |
| เค้ก (Cake) | อาทิตย์ที่ 22 มี.ค. | 18.3 ชิ้น | 19.2 ชิ้น | 0.31 กก. |

---

## 1.3 วัตถุประสงค์ของโครงงาน

1. พัฒนาระบบ AI สำหรับพยากรณ์ความต้องการอาหารรายวันแบบ per-item โดยอิงข้อมูลประวัติยอดขายจริง
2. สร้าง MLOps Pipeline ครบวงจร ตั้งแต่การเตรียมข้อมูล ฝึกโมเดล ติดตาม experiment จนถึงการ deploy ออนไลน์
3. ลดปริมาณขยะอาหารในธุรกิจร้านอาหารและโรงอาหาร ด้วยการแนะนำปริมาณการเตรียมที่เหมาะสม
4. พัฒนา Dashboard ภาษาไทยที่ใช้งานง่าย ให้เจ้าหน้าที่โรงอาหารสามารถใช้ประโยชน์ได้จริงโดยไม่ต้องมีความรู้ด้านเทคนิค
5. สนับสนุนเป้าหมายการพัฒนาที่ยั่งยืน SDG 2 (Zero Hunger) และ SDG 12 (Responsible Consumption) ของสหประชาชาติ

---

## 1.4 ขอบเขตของโครงงาน

**ขอบเขตที่ครอบคลุม:**
- ข้อมูลยอดขายจากร้านเบเกอรี่ 20,507 รายการ ช่วง ต.ค. 2016 – เม.ย. 2017
- รองรับ 10 รายการสินค้าขายดีที่สุด: Bread, Brownie, Cake, Coffee, Cookies, Hot Chocolate, Medialuna, Pastry, Sandwich, Tea
- การพยากรณ์อิงจาก 4 features: วันในสัปดาห์, สถานะวันหยุด, เดือน, วันที่ในเดือน
- Safety Stock กำหนดที่ 5% และ Waste reduction factor ที่ 0.35 กก./หน่วย
- Deploy backend บน Render.com และ frontend บน Streamlit Community Cloud

**ขอบเขตที่ไม่ครอบคลุม:**
- การพยากรณ์จากเทศกาล โปรโมชัน หรือสภาพอากาศ
- ข้อมูล real-time จาก POS system
- การเชื่อมต่อกับระบบสั่งซื้อวัตถุดิบอัตโนมัติ
- รายการอาหารที่นอกเหนือจาก 10 รายการที่กำหนด

---

## 1.5 ประโยชน์ที่คาดว่าจะได้รับ

**ประโยชน์เชิงธุรกิจ:**
- ลดต้นทุนจากการสูญเสียอาหารที่เตรียมเกินความต้องการ คาดการณ์ประหยัดได้ 5–15% ของต้นทุนวัตถุดิบ
- ปรับปรุงประสิทธิภาพการวางแผนการผลิต ลดภาระการตัดสินใจของเจ้าหน้าที่
- เปลี่ยนจากการตัดสินใจด้วยความรู้สึก (Gut Feeling) เป็น Data-Driven Decision Making

**ประโยชน์เชิงสังคมและสิ่งแวดล้อม:**
- ลดปริมาณขยะอาหาร ลดการปล่อยก๊าซเรือนกระจก (ประมาณ 2.5 กก. CO₂e ต่อขยะอาหาร 1 กก.)
- Safety Stock +5% ช่วยให้มีอาหารพร้อมบริการสม่ำเสมอ ลดโอกาสที่ลูกค้าไม่ได้รับอาหาร
- สนับสนุนการบริโภคและการผลิตที่มีความรับผิดชอบตาม SDG 12

**ประโยชน์เชิงการศึกษา:**
- เป็นตัวอย่าง MLOps pipeline ครบวงจรสำหรับปัญหาจริง ตั้งแต่ Data Preparation ถึง Production Deployment
- แสดงการทำงานร่วมกันของ PyTorch, Prefect, MLflow, FastAPI, Streamlit และ Docker ใน ecosystem เดียว

---

# บทที่ 2

## 2.1 ระบบพยากรณ์และหลักการทำงาน

ระบบพยากรณ์ความต้องการอาหารทำงานบนหลักการ **Item Mean Normalization** ร่วมกับ **MLP Neural Network** ซึ่งแก้ปัญหาโมเดลเดียวที่ต้องทำนายสินค้าหลายชนิดที่มีปริมาณขายต่างกันมาก

**สถาปัตยกรรมของโมเดล MLP:**

```python
class DemandModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 32),   # Input: 4 features → 32 neurons
            nn.ReLU(),
            nn.Linear(32, 16),  # 32 → 16 neurons
            nn.ReLU(),
            nn.Linear(16, 1),   # 16 → 1 output (normalized demand)
        )
```

**ขั้นตอนการทำงานของระบบ:**

```
ขั้นที่ 1: คำนวณ item_mean = mean(demand) ต่อรายการสินค้า
ขั้นที่ 2: normalize  →  demand_norm = demand / item_mean  (ค่าประมาณ ≈ 1.0)
ขั้นที่ 3: สร้าง 4 features จากวันที่ที่ผู้ใช้เลือก
            day_of_week, is_weekend, month_norm, day_norm
ขั้นที่ 4: โมเดลเรียนรู้ demand_norm จาก 4 features (MLP)
ขั้นที่ 5: inference  →  predicted = MLP(features) × item_mean
ขั้นที่ 6: recommended = predicted × 1.05  (Safety Stock +5%)
ขั้นที่ 7: waste_reduced = (recommended - predicted) × 0.35 กก.
```

**ข้อมูล Training:**

| พารามิเตอร์ | ค่า |
|------------|-----|
| แหล่งข้อมูล | bakery_sales_revised.csv |
| จำนวนรายการ | 20,507 transactions |
| ช่วงเวลา | ต.ค. 2016 – เม.ย. 2017 |
| Daily records (หลัง aggregate) | 1,432 records |
| Optimizer | Adam (lr=0.005) |
| Loss Function | L1Loss (MAE) |
| Epochs | 1,000 |
| Architecture | MLP: 4→32→16→1 |

---

## 2.2 พฤติกรรมการบริโภคอาหารและการแก้ไขปัญหา

**รูปแบบยอดขายที่โมเดลเรียนรู้:**

จากการวิเคราะห์ข้อมูลจริง พบ pattern ดังนี้

| ลักษณะ | รายละเอียด |
|--------|-----------|
| วันธรรมดา vs วันหยุด | Coffee ขายดีวันธรรมดา, Cake/Pastry ขายดีวันหยุด |
| ช่วงเช้า-เย็น | ข้อมูลรวมเป็น daily total ต่อ item |
| ความแปรปรวนรายวัน | วันที่ 1–31 ในเดือนมีผลต่อยอดขายบ้างในบางรายการ |
| ความแตกต่างรายเดือน | ช่วงปลายปี (พ.ย.–ธ.ค.) ยอดขายสูงกว่าต้นปี |

**ค่าเฉลี่ยยอดขายรายวันต่อสินค้า (จากข้อมูลจริง):**

| รายการ | ชื่อไทย | หน่วย | ค่าเฉลี่ย/วัน |
|--------|--------|------|-------------|
| Coffee | กาแฟ | แก้ว | ~34.6 |
| Tea | ชา | แก้ว | ~9.1 |
| Bread | ขนมปัง | ก้อน | ~20.9 |
| Sandwich | แซนด์วิช | ชิ้น | ~5.0 |
| Cake | เค้ก | ชิ้น | ~7.0 |
| Pastry | เพสทรี่ | ชิ้น | ~5.7 |
| Medialuna | มีเดียลูนา (ครัวซอง) | ชิ้น | ~4.7 |
| Cookies | คุกกี้ | ชิ้น | ~3.8 |
| Hot Chocolate | ช็อกโกแลตร้อน | แก้ว | ~4.0 |
| Brownie | บราวนี่ | ชิ้น | ~4.5 |

**วงจรขยะอาหารที่ระบบช่วยตัดออก:**

```
เดิม: เตรียมตามความรู้สึก (50 แก้ว) → ขายได้ 34 → ทิ้ง 16 แก้ว = 5.6 กก.
ใหม่: ระบบแนะนำ 35.8 แก้ว → ขายได้ 34 → เหลือ 1.8 แก้ว = 0.6 กก.
ลดขยะได้: 5.0 กก./วัน ต่อ 1 รายการ
```

---

## 2.3 โครงสร้างโปรเจกต์

```
MLOPS Project/
├── src/
│   ├── pipeline.py          # Prefect flow: load → train → MLflow → save
│   └── api.py               # FastAPI: /health, /items, /predict
├── app.py                   # Streamlit dashboard (ภาษาไทย)
├── data/
│   └── bakery_sales_revised.csv   # ข้อมูลยอดขายจริง 20,507 รายการ
├── models/                  # สร้างจาก pipeline.py
│   ├── demand_model.pth     # MLP model weights (PyTorch)
│   └── item_map.json        # { "Coffee": {"idx":0, "mean":34.6}, ... }
├── requirements.txt         # Python dependencies (>=version)
├── Dockerfile               # CPU-only torch → image ~800MB
├── docker-compose.yml       # 3 services: mlflow, backend, frontend
├── .gitignore               # ไม่รวม .venv/, data/, mlruns/, .prefect/
└── pyrightconfig.json       # Suppress Pylance type warnings
```

**คำอธิบายไฟล์หลัก:**

**`src/pipeline.py`** — MLOps Training Pipeline (Prefect Flow)
```
_load_data()     → อ่าน CSV, สร้าง 4 features, normalize demand
_train_model()   → ฝึก MLP 1,000 epochs, คำนวณ MAE
log_to_mlflow()  → บันทึก params + metrics ลง MLflow (DagsHub)
save_model()     → บันทึก demand_model.pth + item_map.json
```

**`src/api.py`** — FastAPI Backend
```
GET /health  → ตรวจสอบสถานะ server
GET /items   → คืนรายการสินค้าทั้งหมดจาก item_map
GET /predict → รับ day_of_week, is_weekend, month, day, item
              → คืน predicted_demand, recommended_qty, waste_reduced_kg
```

**`app.py`** — Streamlit Frontend (ภาษาไทย)
```
- เชื่อมต่อ FastAPI ผ่าน API_URL environment variable
- Date picker + Item selectbox (ชื่อไทย + หน่วยที่ถูกต้อง)
- แสดงผล 3 metric cards + API response expander
```

---

## 2.4 สถาปัตยกรรมระบบ (System Architecture)

```
┌─────────────────────────────────────────────────────────────┐
│                    TRAINING PIPELINE                        │
│                                                             │
│  bakery_sales_revised.csv                                   │
│         ↓                                                   │
│  Prefect Flow (pipeline.py)                                 │
│  ├── _load_data()   → 4 features + item_mean normalization  │
│  ├── _train_model() → MLP 4→32→16→1, Adam, L1Loss, 1000ep  │
│  ├── log_to_mlflow()→ DagsHub MLflow tracking               │
│  └── save_model()   → models/demand_model.pth               │
│                        models/item_map.json                 │
└────────────────────────┬────────────────────────────────────┘
                         │ model artifacts
                         ▼
┌────────────────────────────────────────────────────────────┐
│                    SERVING LAYER                            │
│                                                             │
│  FastAPI Backend (Render.com : port 8000)                  │
│  ├── GET /health   → {"status": "ok"}                      │
│  ├── GET /items    → {"items": ["Bread", "Coffee", ...]}   │
│  └── GET /predict  → {predicted_demand, recommended_qty,   │
│                        waste_reduced_kg, ...}              │
│              ↑ HTTP                                         │
│  Streamlit Dashboard (Streamlit Cloud : port 8501)         │
│  ├── Date picker + Item selectbox (Thai UI)                 │
│  └── 3 Metric cards: คาดการณ์ | แนะนำ | ขยะลดได้          │
└────────────────────────────────────────────────────────────┘
                         │
┌────────────────────────▼───────────────────────────────────┐
│                    MONITORING                               │
│  MLflow UI บน DagsHub                                      │
│  Track: epochs, lr, features, MAE_normalized, n_records    │
│  Compare runs, Roll back to best model                     │
└────────────────────────────────────────────────────────────┘
```

**Deployment Architecture:**

| Component | Platform | URL |
|-----------|----------|-----|
| FastAPI Backend | Render.com (Docker) | food-waste-api-2lbr.onrender.com |
| Streamlit Frontend | Streamlit Cloud | mlops-project-...streamlit.app |
| MLflow Tracking | DagsHub | dagshub.com/.../mlops-project.mlflow |

---

## 2.5 เทคโนโลยีและเครื่องมือที่ใช้ในการพัฒนา

### Machine Learning

**PyTorch 2.4+**
- Framework หลักสำหรับสร้างและฝึก MLP Neural Network
- Architecture: `nn.Sequential` → `nn.Linear` → `nn.ReLU`
- Optimizer: `Adam (lr=0.005)` / Loss: `L1Loss` (MAE)
- ติดตั้งแบบ CPU-only ลดขนาด Docker image จาก ~3GB เหลือ ~800MB
- ใช้ `torch.save` / `torch.load` สำหรับ model serialization

**Pandas 2.2+ / NumPy 1.26+**
- Pandas: อ่าน CSV, parse datetime, groupby aggregate daily demand
- NumPy: แปลง DataFrame เป็น float32 array ก่อนส่งเข้า PyTorch tensor

### MLOps Tools

**Prefect 2.20+**
- Workflow Orchestration สำหรับ training pipeline
- ใช้ `@flow` ครอบ pipeline ทั้งหมด, `@task` แยกแต่ละขั้นตอน
- ตั้ง `PREFECT_HOME` ในโปรเจกต์เพื่อหลีกเลี่ยง SQLite permission error
- บันทึก logs และติดตามสถานะ run ของแต่ละขั้นตอน

**MLflow 2.14+**
- Experiment Tracking: บันทึก hyperparameters + metrics ทุก run
- Tracking URI: DagsHub remote server (`https://dagshub.com/...mlflow`)
- Log params: `epochs`, `lr`, `features`, `target`, `n_training_records`
- Log metric: `MAE_normalized`
- ดู experiment history ผ่าน MLflow UI บน DagsHub

### Backend API

**FastAPI 0.111+**
- REST API แบบ async ด้วย Python
- Auto-generate Swagger UI ที่ `/docs` สำหรับทดสอบ API
- Query Parameter validation อัตโนมัติ (type + range check)
- Error handling ด้วย `HTTPException` status 422

**Uvicorn 0.30+**
- ASGI server สำหรับรัน FastAPI
- ใช้ `--host 0.0.0.0 --port 8000` สำหรับ production

### Frontend Dashboard

**Streamlit 1.36+**
- สร้าง Web Dashboard ด้วย Python ล้วน ไม่ต้องเขียน HTML/CSS
- ใช้ `st.date_input`, `st.selectbox`, `st.metric`, `st.spinner`
- `@st.cache_data(ttl=60)` cache รายการสินค้าจาก API
- รองรับภาษาไทยทั้งหมด พร้อม unit ที่ถูกต้อง (แก้ว/ชิ้น/ก้อน)

### Containerization & Deployment

**Docker + Docker Compose**
- `python:3.10-slim` base image
- ติดตั้ง PyTorch CPU-only ก่อนเพื่อ optimize layer caching
- `COPY models/ ./models/` เพื่อ bundle model artifacts เข้า image
- Healthcheck ใช้ Python urllib (ไม่มี curl ใน slim image)
- Docker Compose: 3 services (mlflow, backend, frontend)

### สรุป Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Model | PyTorch MLP | ≥ 2.4 |
| Pipeline Orchestration | Prefect | ≥ 2.20 |
| Experiment Tracking | MLflow + DagsHub | ≥ 2.14 |
| Data Processing | Pandas + NumPy | ≥ 2.2 / ≥ 1.26 |
| Backend API | FastAPI + Uvicorn | ≥ 0.111 / ≥ 0.30 |
| Frontend | Streamlit | ≥ 1.36 |
| Containerization | Docker + Compose | latest |
| Backend Hosting | Render.com | - |
| Frontend Hosting | Streamlit Cloud | - |
| MLflow Hosting | DagsHub | - |
| Language | Python | 3.10 |

---

# บทที่ 3

## Target Users / Target Market

### 3.1 กลุ่มเป้าหมาย (Target Users / Target Market)

**กลุ่มเป้าหมายหลัก (Primary Users):**

**1. เจ้าหน้าที่โรงอาหารในมหาวิทยาลัยและโรงเรียน**
- ต้องการทราบว่าแต่ละวันควรเตรียมเมนูใดเป็นจำนวนเท่าใด
- ไม่มีความเชี่ยวชาญด้าน Data Science แต่ต้องการผลลัพธ์ที่นำไปใช้งานได้ทันที
- ต้องการ Dashboard ภาษาไทยที่เข้าใจง่าย แสดงผลเป็นหน่วยที่คุ้นเคย (แก้ว/ชิ้น/ก้อน)

**2. เจ้าของและผู้จัดการร้านเบเกอรี่ขนาดเล็ก-กลาง**
- ต้องการลดของเสียจากการเตรียมเกิน เพื่อเพิ่มกำไร
- สนใจ Data-Driven approach แต่ไม่มีทีม IT หรืองบลงทุนด้านเทคโนโลยีสูง
- ต้องการระบบที่เชื่อถือได้ ราคาถูก (ฟรี) และ deploy ง่าย

**3. ฝ่ายจัดซื้อและวางแผนของโรงแรม/โรงพยาบาล**
- ต้องการระบบช่วยวางแผนสั่งซื้อวัตถุดิบล่วงหน้า
- ลดของเสียในแผนกอาหาร ซึ่งเป็นต้นทุนหลักขององค์กร
- ต้องการ audit trail ว่าใช้ข้อมูลอะไรในการตัดสินใจ (MLflow ช่วยตรงนี้)

**กลุ่มเป้าหมายรอง (Secondary Users):**

**4. นักศึกษาและนักวิจัยด้าน MLOps / AI**
- ใช้เป็น reference implementation ของ MLOps pipeline ครบวงจร
- ศึกษาการใช้ PyTorch, Prefect, MLflow, FastAPI, Streamlit ร่วมกัน

**5. องค์กรด้านความยั่งยืน (NGOs / CSR Teams)**
- ต้องการเครื่องมือช่วย track และลด food waste ขององค์กรพันธมิตร
- แสดงผลกระทบต่อสิ่งแวดล้อมเป็นตัวเลข (กก. CO₂e) ได้จริง

**ขนาดตลาด (ประเทศไทย):**

| กลุ่ม | ประมาณการ |
|------|---------|
| โรงอาหารในสถานศึกษา | > 2,000 แห่ง |
| ร้านเบเกอรี่ขนาดเล็ก-กลาง | > 50,000 ร้าน |
| โรงแรม 3-5 ดาว | > 3,000 แห่ง |
| โรงพยาบาลที่มีโรงอาหาร | > 1,000 แห่ง |

---

# บทที่ 4

## Social Impact & Assessment

### 4.1 ผลลัพธ์ทางสังคมที่เกิดขึ้น

**มิติที่ 1 — สิ่งแวดล้อม (Environmental Impact)**

อาหาร 1 กิโลกรัมที่ถูกทิ้งปล่อยก๊าซเรือนกระจกประมาณ **2.5 กก. CO₂e** (FAO, 2013) หากระบบนี้ช่วยให้โรงอาหาร 1 แห่งลดของเสียได้เพียงวันละ 5 กก. จะลด CO₂e ได้ถึง **4,562 กก./ปี** เทียบเท่ากับปลูกต้นไม้กว่า 200 ต้น

**มิติที่ 2 — เศรษฐกิจ (Economic Impact)**

| ประเภทผลประโยชน์ | มูลค่าประมาณ |
|----------------|------------|
| ลดต้นทุนวัตถุดิบสูญเสีย | 5–15% ของต้นทุนอาหาร |
| ตัวอย่าง: ร้านมีต้นทุน 50,000 บาท/เดือน | ประหยัด ~5,000 บาท/เดือน |
| ประหยัดต่อปี | ~60,000 บาท/ปี ต่อร้าน |

**มิติที่ 3 — สังคม (Social Impact)**

**SDG 2 — Zero Hunger:**
- Safety Stock +5% ช่วยให้มีอาหารพร้อมบริการสม่ำเสมอ ลดโอกาสที่ลูกค้าไม่ได้รับอาหาร
- อาหารที่ "เหลือแบบมีการวางแผน" สามารถบริจาคให้ผู้ที่ต้องการก่อนทิ้ง
- เปลี่ยนวัฏจักรจาก "เตรียมมากเกิน → ทิ้ง" เป็น "เตรียมพอดี → ลูกค้าได้ทุกคน"

**SDG 12 — Responsible Consumption:**
- เปลี่ยนการตัดสินใจจาก Gut Feeling เป็น Data-Driven อย่างยั่งยืน
- แสดงตัวเลขขยะที่ลดได้ (กก.) ทุก prediction สร้าง awareness ด้านสิ่งแวดล้อมในองค์กร
- สร้างวัฒนธรรมการลดขยะที่วัดผลได้จริงในระดับองค์กร

---

### 4.2 วิธีการวัดผล

**KPIs หลักของระบบ:**

| KPI | วิธีวัด | เป้าหมาย |
|-----|---------|---------|
| MAE (Normalized) | จาก MLflow metric | < 0.30 |
| ปริมาณขยะที่ลดได้ (กก./วัน) | จาก waste_reduced_kg API | > 2 กก./วัน |
| ความแม่นยำ | เปรียบเทียบกับยอดขายจริง | ±15% |
| System Uptime | Monitor จาก /health endpoint | > 99% |

**วิธีประเมิน Accuracy ของโมเดล:**

```
ข้อมูลที่มี:  ต.ค. 2016 – เม.ย. 2017 (7 เดือน)
Train split:  80% (ต.ค. 2016 – ม.ค. 2017)
Test split:   20% (ก.พ. 2017 – เม.ย. 2017)
Metric:       MAE Normalized = mean(|predicted_norm - actual_norm|)
```

**ตัวอย่างการคำนวณ Waste Reduction:**

```
ก่อนใช้ระบบ:
  เตรียม Coffee 50 แก้ว → ขายได้ 34 → ทิ้ง 16 แก้ว → 5.6 กก. ขยะ

หลังใช้ระบบ:
  ระบบแนะนำ 35.8 แก้ว → ขายได้ 34 → เหลือ 1.8 แก้ว → 0.6 กก. ขยะ

ลดขยะได้ = 5.0 กก./วัน ต่อ 1 รายการ
```

**แผนติดตามผลระยะยาว:**
- Retrain โมเดลทุก 3 เดือน เมื่อมีข้อมูลใหม่สะสม
- ใช้ MLflow เปรียบเทียบ MAE ระหว่าง runs เพื่อเลือก best model
- เก็บ feedback จากผู้ใช้งานจริงเพื่อปรับปรุง safety stock factor

---

# บทที่ 5

## Team

โครงงานนี้พัฒนาโดยนักศึกษา 2 คน รับผิดชอบในแต่ละด้านดังนี้

| | **ผู้พัฒนาที่ 1** | **ผู้พัฒนาที่ 2** |
|-|----------------|----------------|
| **ชื่อ** | Palus Kaewaram | Natthapol Aiemburanont |
| **รหัสนักศึกษา** | 66070131 | 66070062 |
| **บทบาท** | Full-Stack MLOps Developer | System Designer & Architect |

**ความรับผิดชอบของ Palus Kaewaram (66070131):**

| ด้าน | งานที่ทำ |
|------|---------|
| Data Engineering | วิเคราะห์ข้อมูล CSV, Feature engineering (4 features), Normalization |
| Machine Learning | ออกแบบ MLP architecture, Item mean scaling, Hyperparameter tuning |
| MLOps Pipeline | Prefect flow, MLflow tracking (DagsHub), Model artifact management |
| Backend Development | FastAPI server, Prediction logic, Validation + Error handling |
| Frontend Development | Streamlit UI ภาษาไทย, Thai item/unit mapping |
| DevOps | Dockerfile (CPU-only), docker-compose, Render + Streamlit Cloud deployment |
| Documentation | README, report.md, code comments |

**ความรับผิดชอบของ Natthapol Aiemburanont (66070062):**

| ด้าน | งานที่ทำ |
|------|---------|
| System Design | คิดระบบและออกแบบ workflow การทำงาน |
| Architecture | ออกแบบสถาปัตยกรรมระบบโดยรวม |
| Requirements | กำหนดความต้องการและขอบเขตของโปรเจกต์ |

---

# บทที่ 6

## Sustainability / Unfair Advantage

### 6.1 Sustainability (ความยั่งยืนของโครงการ)

**ความยั่งยืนด้านเทคนิค:**

**1. Automated Retraining Pipeline**
ระบบมี Prefect training pipeline ที่พร้อม retrain ทันที เมื่อมีข้อมูลใหม่ เพียงวาง CSV ใหม่ใน `data/` แล้วรัน:
```bash
python src/pipeline.py
```
โมเดลและ `item_map.json` จะถูก update อัตโนมัติ พร้อมบันทึก run ใหม่ลง MLflow

**2. Experiment Tracking ด้วย MLflow + DagsHub**
ทุก training run ถูกบันทึกบน DagsHub ทำให้สามารถ:
- เปรียบเทียบ MAE ระหว่าง runs เพื่อเลือก best model
- Roll back ไปใช้ model เวอร์ชันก่อนหน้าได้ทันที
- Share experiment history กับทีมโดยไม่ต้อง setup server

**3. Containerized Deployment ด้วย Docker**
ระบบทั้งหมดรันบน Docker container ทำให้:
- Deploy ได้ทุก platform ที่รัน Docker (ไม่ขึ้นกับ OS)
- Reproducible environment — ไม่มีปัญหา "runs on my machine"
- Scale ได้ง่ายโดยเพิ่ม replicas

**4. Modular Architecture**
แต่ละส่วนแยกจากกันชัดเจน:
- เปลี่ยนโมเดลจาก MLP เป็น LSTM ได้โดยแก้เฉพาะ `pipeline.py` + `api.py`
- เพิ่มรายการอาหารได้โดย retrain ด้วยข้อมูลใหม่ ไม่ต้องแก้โค้ด
- เปลี่ยน frontend จาก Streamlit เป็น React ได้โดยไม่กระทบ backend

**ความยั่งยืนด้านธุรกิจ:**

**1. Data Flywheel — ข้อมูลที่ดีขึ้นตามเวลา**
ยิ่งใช้งานนาน ยิ่งมีข้อมูลสะสมมากขึ้น โมเดลที่ retrain ด้วยข้อมูลใหม่จะแม่นยำกว่าเดิม

**2. ต้นทุน Infrastructure ต่ำมาก**
- Render.com Free Tier: FastAPI backend (ฟรี)
- Streamlit Community Cloud: Frontend (ฟรี)
- DagsHub: MLflow tracking (ฟรี)
- ไม่ต้องการ GPU ทั้ง training และ inference

**3. Roadmap การพัฒนาต่อเนื่อง**

| Phase | Feature |
|-------|---------|
| Phase 2 | LINE Notify แจ้งเตือนปริมาณที่ควรเตรียมทุกเช้า |
| Phase 3 | เชื่อมต่อ POS system รับข้อมูล real-time |
| Phase 4 | รองรับหลายสาขา (multi-location) |
| Phase 5 | เพิ่ม features: อุณหภูมิ, เทศกาล, โปรโมชัน |

---

### 6.2 Unfair Advantage (ข้อได้เปรียบที่คู่แข่งเลียนแบบได้ยาก)

**1. Item Mean Normalization + MLP Architecture**

สถาปัตยกรรมโมเดลที่ออกแบบมาเฉพาะสำหรับปัญหานี้ ทำให้โมเดลเดียวรองรับสินค้าทุกชนิดได้โดยไม่ต้องสร้างโมเดลแยก MLP จับ non-linear patterns ที่ Linear Regression ทำไม่ได้ ทำให้แต่ละวันได้ค่าที่แตกต่างกันตามความเป็นจริง

**2. Thai-First UX Design**

Dashboard ออกแบบมาสำหรับผู้ใช้ไทยโดยเฉพาะ:
- ชื่อสินค้าภาษาไทยครบถ้วน
- หน่วยที่ถูกต้องตามบริบทไทย (แก้ว/ชิ้น/ก้อน)
- วันในสัปดาห์ภาษาไทย (วันจันทร์–วันอาทิตย์)
- ข้อความ error และ help text ภาษาไทย

**3. Production-Ready MLOps Stack**

ไม่ใช่แค่ prototype แต่มีทุกองค์ประกอบของ production system:
- Experiment tracking + versioning (MLflow + DagsHub)
- Containerized deployment (Docker)
- Health check endpoint สำหรับ monitoring
- Graceful error handling ทั้ง API และ frontend
- Environment variable configuration สำหรับ multi-environment

**4. Measurable Environmental Impact**

ระบบแสดงตัวเลข **"ขยะที่ลดได้ (กก.)"** โดยตรงในทุก prediction ทำให้ผู้ใช้เห็น environmental impact ทันที สร้าง behavioral change ได้จริงมากกว่าระบบที่แค่แสดงตัวเลขพยากรณ์อย่างเดียว

**5. Zero Dependency on External AI Services**

โมเดลรันบน CPU ใน container เอง ทำให้:
- ไม่มีค่าใช้จ่าย per-request (ต่างจาก OpenAI API)
- ข้อมูลไม่ถูกส่งออกนอกองค์กร (Data Privacy)
- ทำงานได้แม้ไม่มี internet (offline inference)
- ไม่ขึ้นอยู่กับ third-party service availability

**6. Full Traceability**

ทุกการทำนายสามารถ trace ย้อนกลับได้ว่าใช้ model version ไหน trained จากข้อมูล run ใด ด้วย MLflow experiment ID ซึ่งเหมาะสำหรับองค์กรที่ต้องการ accountability ในการตัดสินใจ

---

*รายงานฉบับนี้จัดทำขึ้นเพื่อประกอบโครงงาน MLOps*
*พัฒนาด้วย PyTorch · Prefect · MLflow · FastAPI · Streamlit · Docker*
*สนับสนุน SDG 2 (Zero Hunger) และ SDG 12 (Responsible Consumption)*

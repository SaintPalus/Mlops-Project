# รายงานโครงงาน
# 🍱 ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ
## Food Waste Prediction & Optimization Planner

**ผู้พัฒนา:** Palus Kaewaram
**รหัสนักศึกษา:** 66070131
**วิชา:** MLOps

---

## สารบัญ

| บทที่ | หัวข้อ | หน้า |
|-------|--------|------|
| **บทที่ 1** | **บทนำ** | 1 |
| 1.1 | ความเป็นมาของปัญหา (Problem Statement) | 1 |
| 1.2 | การแก้ไขปัญหา (Solution) | 2 |
| 1.3 | วัตถุประสงค์ของโครงงาน | 3 |
| 1.4 | ขอบเขตของโครงงาน | 3 |
| 1.5 | ประโยชน์ที่คาดว่าจะได้รับ | 4 |
| **บทที่ 2** | **รายละเอียดระบบ** | 5 |
| 2.1 | ระบบพยากรณ์และหลักการทำงาน | 5 |
| 2.2 | ปัญหาขยะอาหารและการแก้ไข | 6 |
| 2.3 | โครงสร้างโปรเจกต์ | 7 |
| 2.4 | สถาปัตยกรรมระบบ (System Architecture) | 8 |
| 2.5 | เทคโนโลยีและเครื่องมือที่ใช้ในการพัฒนา | 9 |
| **บทที่ 3** | **กลุ่มเป้าหมาย (Target Users / Target Market)** | 11 |
| 3.1 | กลุ่มเป้าหมาย | 11 |
| **บทที่ 4** | **Social Impact & Assessment** | 12 |
| 4.1 | ผลลัพธ์ทางสังคมที่เกิดขึ้น | 12 |
| 4.2 | วิธีการวัดผล | 13 |
| **บทที่ 5** | **Team** | 14 |
| **บทที่ 6** | **Sustainability / Unfair Advantage** | 15 |
| 6.1 | Sustainability (ความยั่งยืนของโครงการ) | 15 |
| 6.2 | Unfair Advantage (ข้อได้เปรียบที่คู่แข่งเลียนแบบได้ยาก) | 16 |

---

# บทที่ 1

## 1.1 ความเป็นมาของปัญหา (Problem Statement)

ปัญหา **ขยะอาหาร (Food Waste)** เป็นหนึ่งในวิกฤตที่โลกกำลังเผชิญอยู่ในปัจจุบัน องค์การอาหารและเกษตรแห่งสหประชาชาติ (FAO) รายงานว่าอาหารประมาณ **1 ใน 3 ของอาหารที่ผลิตทั่วโลก** หรือราว **1.3 พันล้านตันต่อปี** ถูกทิ้งเป็นขยะโดยเปล่าประโยชน์ ในขณะที่ประชากรกว่า **800 ล้านคน** ยังคงประสบปัญหาการขาดแคลนอาหาร

สำหรับธุรกิจร้านอาหารและโรงอาหาร ปัญหาหลักที่พบบ่อย ได้แก่:

- **การเตรียมอาหารเกินความต้องการ:** เจ้าของร้านไม่มีข้อมูลที่แม่นยำเพียงพอในการพยากรณ์ว่าแต่ละวันควรเตรียมรายการอาหารแต่ละชนิดเป็นจำนวนเท่าใด จึงมักเตรียมเผื่อไว้มาก ทำให้เกิดของเหลือและต้องทิ้งในภายหลัง
- **ขาดเครื่องมือวิเคราะห์ข้อมูล:** ธุรกิจขนาดเล็กส่วนใหญ่ยังคงพึ่งพาการตัดสินใจจากประสบการณ์และความรู้สึก (gut feeling) มากกว่าการใช้ข้อมูลจริง
- **ความผันผวนตามวันในสัปดาห์:** ยอดขายสินค้าแต่ละรายการมีความแตกต่างกันอย่างมีนัยสำคัญระหว่างวันธรรมดาและวันหยุดสุดสัปดาห์ ซึ่งหากไม่มีการวิเคราะห์ที่ดีจะทำให้เกิดการขาดหรือเกินอย่างหลีกเลี่ยงไม่ได้
- **ผลกระทบทางเศรษฐกิจ:** ขยะอาหารไม่ใช่แค่ปัญหาสิ่งแวดล้อม แต่ยังหมายถึงต้นทุนที่สูญเสียไปโดยตรง ซึ่งกระทบต่อกำไรของธุรกิจโดยตรง

ปัญหาเหล่านี้สอดคล้องกับ **เป้าหมายการพัฒนาที่ยั่งยืน (SDGs)** ของสหประชาชาติ 2 ข้อ ได้แก่:

> **SDG 2 — Zero Hunger:** ขจัดความหิวโหย บรรลุความมั่นคงทางอาหาร ปรับปรุงโภชนาการ และส่งเสริมเกษตรกรรมที่ยั่งยืน

> **SDG 12 — Responsible Consumption and Production:** สร้างแบบแผนการบริโภคและการผลิตที่ยั่งยืน โดยมีเป้าหมายย่อย 12.3 ระบุว่าต้องลดการสูญเสียและขยะอาหารในระดับค้าปลีกและผู้บริโภคลงครึ่งหนึ่งภายในปี 2030

---

## 1.2 การแก้ไขปัญหา (Solution)

โครงงานนี้พัฒนา **ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ** โดยนำหลักการ **MLOps (Machine Learning Operations)** มาประยุกต์ใช้ในการสร้างระบบ AI ที่สามารถพยากรณ์ยอดขายรายวันของรายการอาหารแต่ละชนิดได้อย่างแม่นยำ

**แนวทางการแก้ไขปัญหา:**

**ขั้นที่ 1 — การเก็บและประมวลผลข้อมูล**
นำข้อมูลยอดขายจริงจากร้านเบเกอรี่จำนวน 20,507 รายการ ครอบคลุมช่วง ต.ค. 2016 – เม.ย. 2017 มาวิเคราะห์ และจัดกลุ่มเป็นยอดขายรายวันต่อรายการอาหาร (daily demand per item)

**ขั้นที่ 2 — การฝึกโมเดล AI**
ใช้ **PyTorch Linear Regression** เรียนรู้รูปแบบ (pattern) ของยอดขายตามวันในสัปดาห์ โดยแบ่งเป็น:
- **Features:** `day_of_week` (0=จันทร์ ... 6=อาทิตย์) และ `is_weekend` (0=วันธรรมดา, 1=วันหยุด)
- **Target:** Normalized demand (demand หารด้วย item historical mean ≈ 1.0)
- **Inference:** ผลลัพธ์ของโมเดล × ค่าเฉลี่ยยอดขายจริงของสินค้านั้น = ยอดขายที่คาดการณ์

**ขั้นที่ 3 — การบริการผ่าน API**
สร้าง REST API ด้วย FastAPI มี endpoint `/predict` รับพารามิเตอร์วัน + ชนิดอาหาร และส่งคืน:
- ยอดขายที่คาดการณ์
- ปริมาณแนะนำ (+5% Safety Stock)
- น้ำหนักขยะที่ลดได้ (กก.)

**ขั้นที่ 4 — Dashboard สำหรับผู้ใช้งาน**
พัฒนาหน้าเว็บภาษาไทยด้วย Streamlit ให้เจ้าหน้าที่โรงอาหารใช้งานได้ง่ายโดยไม่ต้องมีความรู้ด้านเทคนิค

**ขั้นที่ 5 — MLOps Pipeline**
ใช้ Prefect จัดการ workflow การฝึกโมเดลและ MLflow บันทึก experiment เพื่อให้สามารถ track ประสิทธิภาพของโมเดลและ retrain ได้ในอนาคต

**ตัวอย่างผลลัพธ์ที่ระบบให้:**

| รายการ | วัน | ยอดขายที่คาดการณ์ | ปริมาณแนะนำ | ขยะที่ลดได้ |
|--------|-----|-------------------|-------------|------------|
| Coffee | วันจันทร์ | 34.1 แก้ว | 35.8 แก้ว | 0.60 กก. |
| Bread | วันเสาร์ | 28.7 ก้อน | 30.1 ก้อน | 0.49 กก. |
| Cake | วันอาทิตย์ | 18.3 ชิ้น | 19.2 ชิ้น | 0.31 กก. |

---

## 1.3 วัตถุประสงค์ของโครงงาน

1. พัฒนาระบบ AI สำหรับพยากรณ์ความต้องการอาหารรายวันโดยอิงข้อมูลประวัติยอดขายจริง
2. สร้าง MLOps Pipeline ที่ครบวงจร ตั้งแต่การเตรียมข้อมูล ฝึกโมเดล ติดตาม experiment จนถึงการ deploy
3. ลดปริมาณขยะอาหารในธุรกิจโรงอาหารด้วยการแนะนำปริมาณการเตรียมที่เหมาะสม
4. พัฒนา Dashboard ภาษาไทยที่ใช้งานง่าย เพื่อให้เจ้าหน้าที่โรงอาหารสามารถใช้ประโยชน์ได้จริง
5. สนับสนุนเป้าหมายการพัฒนาที่ยั่งยืน SDG 2 และ SDG 12 ของสหประชาชาติ

---

## 1.4 ขอบเขตของโครงงาน

**ขอบเขตที่ครอบคลุม:**
- ข้อมูลยอดขายจากร้านเบเกอรี่ครอบคลุม 10 รายการขายดีที่สุด ได้แก่ Bread, Brownie, Cake, Coffee, Cookies, Hot Chocolate, Medialuna, Pastry, Sandwich, Tea
- การพยากรณ์อิงจาก 2 features คือ วันในสัปดาห์ (day_of_week) และสถานะวันหยุด (is_weekend)
- ระบบรองรับการพยากรณ์ล่วงหน้าสูงสุด 1 รายการต่อการ query
- ตัวเลข Safety Stock กำหนดที่ 5% และ Waste reduction factor ที่ 0.35 กก. ต่อหน่วย

**ขอบเขตที่ไม่ครอบคลุม:**
- การพยากรณ์ตามฤดูกาล เทศกาล หรือโปรโมชัน
- ข้อมูล real-time จาก POS system
- การเชื่อมต่อกับระบบบัญชีหรือสั่งซื้อวัตถุดิบอัตโนมัติ
- รายการอาหารที่นอกเหนือจาก 10 รายการที่กำหนด

---

## 1.5 ประโยชน์ที่คาดว่าจะได้รับ

**ประโยชน์เชิงธุรกิจ:**
- ลดต้นทุนจากการสูญเสียอาหารที่เตรียมเกินความต้องการ
- ปรับปรุงประสิทธิภาพการวางแผนการผลิตและการสั่งซื้อวัตถุดิบ
- ลดภาระการตัดสินใจของเจ้าหน้าที่ด้วยการใช้ข้อมูล (Data-Driven Decision Making)

**ประโยชน์เชิงสังคมและสิ่งแวดล้อม:**
- ลดปริมาณขยะอาหารที่ส่งผลกระทบต่อสิ่งแวดล้อม
- ช่วยให้มีอาหารเพียงพอสำหรับลูกค้าโดยไม่ขาดแคลน ผ่าน Safety Stock 5%
- สนับสนุนการบริโภคและการผลิตที่มีความรับผิดชอบตาม SDG 12

**ประโยชน์เชิงการศึกษา:**
- เป็นตัวอย่างการนำ MLOps มาใช้ในปัญหาจริง ตั้งแต่ Data Preparation ถึง Deployment
- แสดงให้เห็นการทำงานร่วมกันของ PyTorch, Prefect, MLflow, FastAPI, Streamlit และ Docker ใน ecosystem เดียว

---

# บทที่ 2

## 2.1 ระบบพยากรณ์และหลักการทำงาน

ระบบพยากรณ์ความต้องการอาหารทำงานบนหลักการ **Item Mean Normalization** ซึ่งแก้ปัญหาโมเดลเดียวที่ต้องทำนายสินค้าหลายชนิดที่มีปริมาณขายต่างกันมาก (Coffee ขายวันละ ~34 แก้ว ขณะที่ Brownie ขายวันละ ~12 ชิ้น)

**หลักการทำงาน:**

```
ขั้นที่ 1: คำนวณ item_mean = mean(demand) ต่อรายการสินค้า จากข้อมูลประวัติ
ขั้นที่ 2: normalize  →  demand_norm = demand / item_mean  (ค่าประมาณ ≈ 1.0)
ขั้นที่ 3: โมเดลเรียนรู้ demand_norm จาก day_of_week และ is_weekend
ขั้นที่ 4: inference  →  predicted = model_output × item_mean (scale กลับ)
ขั้นที่ 5: recommended = predicted × 1.05  (Safety Stock +5%)
ขั้นที่ 6: waste_reduced = (recommended - predicted) × 0.35 กก.
```

**สูตรคำนวณ:**

```
demand_norm(item, day)    = demand(item, day) / mean_demand(item)
predicted_demand(item, d) = LinearRegression(day_of_week, is_weekend) × mean_demand(item)
recommended_qty           = predicted_demand × 1.05
waste_reduced_kg          = (recommended_qty - predicted_demand) × 0.35
```

**โมเดล PyTorch Linear Regression:**

```python
class DemandModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 1)   # 2 features → 1 output

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.linear(x)
```

**ข้อมูลที่ใช้ฝึกโมเดล:**

| พารามิเตอร์ | ค่า |
|------------|-----|
| แหล่งข้อมูล | bakery_sales_revised.csv |
| จำนวนรายการทั้งหมด | 20,507 transactions |
| ช่วงเวลา | ต.ค. 2016 – เม.ย. 2017 |
| รายการที่ใช้ | 10 สินค้าขายดีที่สุด |
| Features | day_of_week (0–6), is_weekend (0/1) |
| Target | demand normalized by item mean |
| Optimizer | Adam (lr=0.01) |
| Loss Function | L1Loss (MAE) |
| Epochs | 300 |

---

## 2.2 ปัญหาขยะอาหารและการแก้ไข

**พฤติกรรมการเกิดขยะอาหารในธุรกิจร้านอาหาร:**

โรงอาหารและร้านเบเกอรี่ส่วนใหญ่เผชิญกับวงจรขยะอาหารดังนี้:

```
เตรียมมากเกินไป → ของเหลือ → ทิ้งตอนปิดร้าน → เสียต้นทุน + เสียสิ่งแวดล้อม
        ↑
เตรียมน้อยเกินไป → ขาดสต็อก → ลูกค้าไม่พอใจ → เสียรายได้
```

**วิธีที่ระบบนี้แก้ปัญหา:**

| ปัญหา | วิธีแก้ไขของระบบ |
|-------|----------------|
| ไม่รู้ว่าแต่ละวันควรเตรียมเท่าไร | พยากรณ์จาก Pattern วันในสัปดาห์โดยใช้ข้อมูลจริง |
| สินค้าต่างชนิดขายต่างปริมาณ | ใช้ Item Mean Scaling ทำให้โมเดลเดียวครอบคลุมทุกสินค้า |
| วันหยุดขายต่างจากวันธรรมดา | มี Feature `is_weekend` แยกการพยากรณ์ |
| กลัวของขาด | บวก Safety Stock +5% อัตโนมัติ |
| ต้องการตัวเลขง่ายๆ | แสดงผลเป็น 3 metric cards บน Dashboard |

**ค่าเฉลี่ยยอดขายรายวันต่อสินค้า (จากข้อมูลจริง):**

| รายการ (ภาษาไทย) | ค่าเฉลี่ยต่อวัน |
|-----------------|---------------|
| Coffee (กาแฟ) | ~34.1 แก้ว |
| Tea (ชา) | ~24.8 แก้ว |
| Bread (ขนมปัง) | ~22.3 ก้อน |
| Sandwich (แซนด์วิช) | ~18.7 ชิ้น |
| Cake (เค้ก) | ~16.4 ชิ้น |
| Pastry (เพสทรี่) | ~15.9 ชิ้น |
| Medialuna (ครัวซอง) | ~14.2 ชิ้น |
| Cookies (คุกกี้) | ~13.5 ชิ้น |
| Hot Chocolate (ช็อกโกแลตร้อน) | ~12.8 แก้ว |
| Brownie (บราวนี่) | ~11.6 ชิ้น |

---

## 2.3 โครงสร้างโปรเจกต์

```
MLOPS Project/
├── src/
│   ├── pipeline.py       # Prefect flow: โหลดข้อมูล → ฝึกโมเดล → MLflow → บันทึก
│   └── api.py            # FastAPI: /health, /items, /predict endpoints
├── app.py                # Streamlit dashboard (ภาษาไทย)
├── data/
│   └── bakery_sales_revised.csv   # ข้อมูลยอดขายจริง 20,507 รายการ
├── models/               # สร้างหลังจาก training
│   ├── demand_model.pth  # PyTorch model weights
│   └── item_map.json     # { "Coffee": {"idx": 0, "mean": 34.1}, ... }
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container image (CPU-only torch ~800MB)
├── docker-compose.yml    # 3 services: mlflow, backend, frontend
├── .gitignore
├── pyrightconfig.json    # Pylance type-check configuration
└── README.md
```

**คำอธิบายไฟล์สำคัญ:**

**`src/pipeline.py`** — หัวใจของ MLOps Pipeline
ประกอบด้วย Prefect Flow ที่ทำงานตามลำดับ:
1. `_load_data()` — อ่าน CSV, คำนวณ daily demand, normalize ด้วย item mean
2. `_train_model()` — ฝึก PyTorch Linear Regression 300 epochs
3. `log_to_mlflow()` — บันทึก parameters + MAE metric ลง MLflow
4. `save_model()` — บันทึก `.pth` + `item_map.json`

**`src/api.py`** — FastAPI Backend
- โหลดโมเดลและ item_map เมื่อ server เริ่มต้น
- `/predict` รับ query parameters และคืนค่าพยากรณ์

**`app.py`** — Streamlit Frontend
- แสดงผลภาษาไทยทั้งหมด พร้อมชื่อสินค้าและหน่วยที่ถูกต้อง
- เชื่อมต่อกับ FastAPI ผ่าน HTTP requests

---

## 2.4 สถาปัตยกรรมระบบ (System Architecture)

```
bakery_sales_revised.csv
        │
        ▼
┌─────────────────┐     ┌──────────────────┐
│  Prefect Flow   │────▶│     MLflow       │
│  (pipeline.py)  │     │  (experiment     │
│                 │     │   tracking)      │
│  1. Load Data   │     └──────────────────┘
│  2. Normalize   │
│  3. Train Model │
│  4. Save .pth   │
└────────┬────────┘
         │ models/demand_model.pth
         │ models/item_map.json
         ▼
┌─────────────────┐     HTTP /predict      ┌─────────────────┐
│   FastAPI       │◀───────────────────────│   Streamlit     │
│   Backend       │                        │   Dashboard     │
│                 │  {                     │                 │
│  /health        │    predicted_demand,   │  วันที่ picker  │
│  /items         │    recommended_qty,    │  เมนูอาหาร      │
│  /predict       │    waste_reduced_kg    │  3 metric cards │
│                 │  }                     │                 │
└─────────────────┘                        └─────────────────┘
     Port 8000                                  Port 8501
```

**การ Deploy ด้วย Docker Compose:**

```
docker-compose.yml
├── mlflow    (port 5000)  — Experiment tracking UI
├── backend   (port 8000)  — FastAPI prediction server
└── frontend  (port 8501)  — Streamlit dashboard
```

---

## 2.5 เทคโนโลยีและเครื่องมือที่ใช้ในการพัฒนา

### Machine Learning & Data Processing

**PyTorch 2.4+**
- Framework สำหรับสร้างและฝึกโมเดล Neural Network
- ใช้ `nn.Linear(2, 1)` เป็น Linear Regression layer
- ใช้ `Adam optimizer` และ `L1Loss` (MAE) เป็น loss function
- เหตุผลที่เลือก: lightweight, รองรับ CPU-only inference, ecosystem กว้าง

**Pandas 2.2+ / NumPy 1.26+**
- ใช้ในการโหลดและ preprocess ข้อมูล CSV
- Group by date/item, คำนวณ daily demand, normalize ข้อมูล

### MLOps Tools

**Prefect 2.20+**
- ใช้เป็น Workflow Orchestration สำหรับ training pipeline
- แบ่ง pipeline เป็น `@task` ย่อยๆ ได้แก่ load data, train, log, save
- ใช้ `@flow` ครอบ task ทั้งหมดเพื่อ orchestrate การทำงาน
- บันทึก log และ track การทำงานของแต่ละ run

**MLflow 2.14+**
- ใช้บันทึก experiment parameters และ metrics
- Track: `epochs`, `lr`, `features`, `n_training_records`, `MAE_normalized`
- Tracking URI แบบ local file store (`./mlruns`)
- สามารถดู experiment history ผ่าน MLflow UI (port 5000)

### Backend API

**FastAPI 0.111+**
- สร้าง REST API ด้วย Python แบบ async
- Auto-generate Swagger UI ที่ `/docs`
- ใช้ Query Parameters สำหรับ `/predict` endpoint
- Validation และ Error handling อัตโนมัติผ่าน Pydantic

**Uvicorn 0.30+**
- ASGI server สำหรับรัน FastAPI
- รองรับ `--reload` สำหรับ development mode

### Frontend Dashboard

**Streamlit 1.36+**
- สร้าง Web Dashboard ด้วย Python ล้วน ไม่ต้องเขียน HTML/CSS
- ใช้ `st.date_input`, `st.selectbox`, `st.metric` สำหรับ UI
- `@st.cache_data` cache รายการสินค้าจาก API เป็นเวลา 60 วินาที
- แสดงผลภาษาไทยทั้งหมด

### Containerization & Deployment

**Docker + Docker Compose**
- Dockerfile ใช้ `python:3.10-slim` base image
- ติดตั้ง PyTorch CPU-only ก่อน ลดขนาด image จาก ~3GB เหลือ ~800MB
- Docker Compose จัดการ 3 containers พร้อมกัน
- Healthcheck ใช้ Python urllib แทน curl (เพื่อความ portable)

### สรุป Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Model Training | PyTorch | ≥ 2.4 |
| Pipeline Orchestration | Prefect | ≥ 2.20 |
| Experiment Tracking | MLflow | ≥ 2.14 |
| Data Processing | Pandas + NumPy | ≥ 2.2 / ≥ 1.26 |
| Backend API | FastAPI + Uvicorn | ≥ 0.111 / ≥ 0.30 |
| Frontend Dashboard | Streamlit | ≥ 1.36 |
| Containerization | Docker + Compose | latest |
| Language | Python | 3.10–3.13 |

---

# บทที่ 3

## Target Users / Target Market

### 3.1 กลุ่มเป้าหมาย (Target Users / Target Market)

**กลุ่มเป้าหมายหลัก (Primary Users):**

**1. เจ้าหน้าที่โรงอาหารและร้านค้าในมหาวิทยาลัย**
- ต้องการทราบว่าแต่ละวันควรเตรียมอาหารเมนูใดเป็นจำนวนเท่าใด
- ไม่มีความเชี่ยวชาญด้านเทคโนโลยีหรือ Data Science
- ต้องการ Dashboard ที่ใช้งานง่าย อ่านผลได้ทันที ด้วยภาษาไทย

**2. เจ้าของและผู้จัดการร้านเบเกอรี่ขนาดเล็ก-กลาง**
- ต้องการลดของเสียจากการเตรียมสินค้าเกินความต้องการ
- สนใจลดต้นทุนการผลิตและเพิ่มกำไร
- ต้องการเครื่องมือที่เชื่อถือได้และใช้ข้อมูลจริง

**3. ผู้บริหารและฝ่ายจัดซื้อของโรงแรม/โรงพยาบาล**
- ต้องการระบบช่วยวางแผนการสั่งซื้อวัตถุดิบล่วงหน้า
- ต้องการลดของเสียในแผนกอาหาร ซึ่งเป็นต้นทุนหลักขององค์กร

**กลุ่มเป้าหมายรอง (Secondary Users):**

**4. นักวิจัยและนักเรียนด้าน MLOps / Data Science**
- ใช้เป็น reference implementation ของ MLOps pipeline ครบวงจร
- ศึกษาการใช้ PyTorch, Prefect, MLflow, FastAPI, Streamlit ร่วมกัน

**5. องค์กรด้านความยั่งยืน (Sustainability Organizations)**
- ต้องการเครื่องมือช่วย track และลด food waste ขององค์กรพันธมิตร

**ขนาดตลาด (Market Size):**

| กลุ่ม | จำนวนประมาณ (ประเทศไทย) |
|------|----------------------|
| โรงอาหารในมหาวิทยาลัยและโรงเรียน | > 2,000 แห่ง |
| ร้านเบเกอรี่ขนาดเล็ก-กลาง | > 50,000 ร้าน |
| โรงแรม (3-5 ดาว) | > 3,000 แห่ง |
| โรงพยาบาลที่มีโรงอาหาร | > 1,000 แห่ง |

---

# บทที่ 4

## Social Impact & Assessment

### 4.1 ผลลัพธ์ทางสังคมที่เกิดขึ้น

ระบบพยากรณ์ความต้องการอาหารสร้างผลกระทบทางสังคมที่วัดได้ใน 3 มิติหลัก:

**มิติที่ 1 — สิ่งแวดล้อม (Environmental Impact)**

การลดขยะอาหาร 1 กิโลกรัมสามารถลดการปล่อยก๊าซคาร์บอนไดออกไซด์ได้ประมาณ 2.5 กก. CO₂e (ที่มา: FAO, 2013) หากระบบนี้ช่วยให้โรงอาหาร 1 แห่งลดของเสียได้เพียงวันละ 5 กก. จะลด CO₂e ได้ถึง **4,562 กก. ต่อปี** ซึ่งเทียบเท่ากับการปลูกต้นไม้กว่า 200 ต้น

**มิติที่ 2 — เศรษฐกิจ (Economic Impact)**

| ประเภทผลประโยชน์ | มูลค่าประมาณ |
|----------------|------------|
| ลดต้นทุนวัตถุดิบที่สูญเสีย | 5–15% ของต้นทุนอาหารทั้งหมด |
| ลดค่าใช้จ่ายในการกำจัดขยะ | ขึ้นอยู่กับขนาดธุรกิจ |
| เพิ่มประสิทธิภาพการวางแผน | ลดเวลาตัดสินใจของเจ้าหน้าที่ |

สำหรับร้านเบเกอรี่ขนาดกลางที่มีต้นทุนวัตถุดิบ 50,000 บาท/เดือน การลดขยะ 10% จะประหยัดได้ **5,000 บาท/เดือน** หรือ **60,000 บาท/ปี**

**มิติที่ 3 — สังคม (Social Impact)**

**SDG 2 — Zero Hunger:**
- Safety Stock 5% ช่วยให้มีอาหารพร้อมบริการสม่ำเสมอ ลดโอกาสที่ลูกค้าไม่ได้รับอาหาร
- อาหารที่ "เหลือแบบมีการวางแผน" สามารถบริจาคให้กับผู้ที่ต้องการได้ก่อนทิ้ง

**SDG 12 — Responsible Consumption:**
- เปลี่ยนการตัดสินใจจากความรู้สึก (intuition) เป็นการใช้ข้อมูล (data-driven)
- สร้างวัฒนธรรมการลดขยะในองค์กร
- ทำให้เห็นตัวเลขขยะที่ลดได้จริงในหน่วยกิโลกรัม ซึ่งช่วยสร้าง awareness

---

### 4.2 วิธีการวัดผล

**KPIs หลักที่ใช้วัด:**

| KPI | วิธีวัด | เป้าหมาย |
|-----|---------|---------|
| MAE (Normalized) | จาก MLflow metric | < 0.20 |
| ปริมาณขยะที่ลดได้ (กก./วัน) | จาก waste_reduced_kg API response | > 2 กก./วัน |
| ความแม่นยำของการพยากรณ์ | เปรียบเทียบกับยอดขายจริงหลัง deploy | ± 15% |
| Uptime ของระบบ | Monitor จาก /health endpoint | > 99% |

**วิธีประเมิน Accuracy ของโมเดล:**

```
ข้อมูลที่มี: ต.ค. 2016 – เม.ย. 2017 (7 เดือน)
ใช้ฝึก: 80% (ต.ค. 2016 – ม.ค. 2017)
ใช้ทดสอบ: 20% (ก.พ. 2017 – เม.ย. 2017)
Metric: MAE (Mean Absolute Error) แบบ normalized
```

**ตัวอย่างการวัดผล waste reduction:**

```
กรณีเดิม (ไม่มีระบบ): เตรียม Coffee 50 แก้ว/วัน → ขายได้ 34 แก้ว → เหลือ 16 แก้ว = 5.6 กก. ขยะ
กรณีใช้ระบบ: เตรียม 35.8 แก้ว → ขายได้ 34 แก้ว → เหลือ 1.8 แก้ว = 0.6 กก. ขยะ
ขยะที่ลดได้: 5.0 กก. ต่อวัน ต่อรายการ
```

**แผนการติดตามผลระยะยาว:**
- Retrain โมเดลทุก 3 เดือน เมื่อมีข้อมูลใหม่สะสมเพียงพอ
- ใช้ MLflow เปรียบเทียบประสิทธิภาพระหว่าง runs
- เก็บ feedback จากผู้ใช้งานจริง (เจ้าหน้าที่โรงอาหาร) เพื่อปรับปรุงโมเดล

---

# บทที่ 5

## Team

โครงงานนี้พัฒนาโดยนักศึกษาเพียงคนเดียว รับผิดชอบทุกส่วนของระบบตั้งแต่ต้นจนถึง deploy

| | รายละเอียด |
|-|-----------|
| **ชื่อ** | Palus Kaewaram |
| **รหัสนักศึกษา** | 66070131 |
| **บทบาท** | Full-Stack MLOps Developer |
| **ความรับผิดชอบ** | Data Pipeline, Model Training, API Development, Frontend, Docker, Deployment |

**บทบาทและหน้าที่ที่รับผิดชอบ:**

| ด้าน | งานที่ทำ |
|------|---------|
| **Data Engineering** | วิเคราะห์ข้อมูล CSV, สร้าง feature engineering, normalize ข้อมูล |
| **Machine Learning** | ออกแบบ PyTorch model, item mean scaling architecture, hyperparameter tuning |
| **MLOps Pipeline** | สร้าง Prefect flow, เชื่อมต่อ MLflow tracking, จัดการ model artifacts |
| **Backend Development** | FastAPI server, prediction logic, error handling |
| **Frontend Development** | Streamlit UI ภาษาไทย, Thai item/unit mapping, responsive layout |
| **DevOps** | Dockerfile, docker-compose.yml, CPU-only optimization |
| **Documentation** | README, report, code comments |

---

# บทที่ 6

## Sustainability / Unfair Advantage

### 6.1 Sustainability (ความยั่งยืนของโครงการ)

**ความยั่งยืนด้านเทคนิค:**

**1. Retraining Pipeline ที่พร้อมใช้งาน**
ระบบมี Prefect training pipeline ที่สามารถรัน retraining ได้ทันทีเมื่อมีข้อมูลใหม่ เพียงแค่วาง CSV ใหม่ใน `data/` folder แล้วรัน:
```bash
python src/pipeline.py
```
โมเดลและ `item_map.json` จะถูก update โดยอัตโนมัติ

**2. Experiment Tracking ด้วย MLflow**
ทุก training run ถูกบันทึกใน MLflow พร้อม parameters และ metrics ทำให้สามารถ:
- เปรียบเทียบว่า model เดิมหรือใหม่ดีกว่ากัน
- Roll back ไปใช้ model เวอร์ชันก่อนหน้าหากจำเป็น
- เลือก best model จากหลาย experiments

**3. Containerization ด้วย Docker**
ระบบทั้งหมดรันบน Docker ทำให้:
- Deploy บน server ใดก็ได้ที่รัน Docker (ไม่ขึ้นกับ OS)
- Scale ได้ง่ายโดยการเพิ่ม replicas
- ไม่มีปัญหา "runs on my machine" เมื่อย้ายระหว่าง environments

**4. Modular Architecture**
แต่ละส่วนแยกจากกันชัดเจน ทำให้ upgrade ได้อิสระ:
- เปลี่ยนโมเดลจาก Linear Regression เป็น LSTM ได้โดยแก้เฉพาะ `pipeline.py` และ `api.py`
- เปลี่ยน Prefect เป็น Airflow ได้โดยไม่กระทบ frontend
- เพิ่มรายการอาหารได้โดยการ retrain ด้วยข้อมูลใหม่

**ความยั่งยืนด้านธุรกิจ:**

**1. ข้อมูลที่ดีขึ้นตามเวลา**
ยิ่งใช้งานนาน ยิ่งมีข้อมูลสะสมมากขึ้น โมเดลที่ retrain ด้วยข้อมูลใหม่จะแม่นยำกว่าเดิม สร้าง positive feedback loop

**2. ต้นทุน Infrastructure ต่ำ**
- Render.com (Free Tier): FastAPI backend ฟรี
- Streamlit Community Cloud: Frontend ฟรี
- ไม่ต้องการ GPU (CPU-only inference)

**3. รองรับการ Extend**
สามารถเพิ่มความสามารถในอนาคต เช่น:
- การแจ้งเตือนอัตโนมัติผ่าน LINE Notify เมื่อถึงเวลาสั่งซื้อ
- เชื่อมต่อกับ POS system เพื่อรับข้อมูล real-time
- เพิ่ม features เช่น อุณหภูมิ, โปรโมชัน, เทศกาล
- รองรับหลายสาขา (multi-location)

---

### 6.2 Unfair Advantage (ข้อได้เปรียบที่คู่แข่งเลียนแบบได้ยาก)

**1. Item Mean Normalization Architecture**
วิธีการ normalize demand ด้วย historical mean ของแต่ละ item แล้วให้โมเดลเรียนรู้ pattern ทำให้โมเดลเดียวรองรับสินค้าทุกชนิดได้โดยไม่ต้องสร้างโมเดลแยก โมเดลเรียนรู้ได้รวดเร็วและ generalize ได้ดีแม้ข้อมูลมีจำกัด

**2. Thai-First UX Design**
Dashboard ออกแบบมาสำหรับผู้ใช้ไทยโดยเฉพาะ ทั้งภาษา หน่วยการวัด (แก้ว/ชิ้น/ก้อน) และวันในสัปดาห์เป็นภาษาไทย ซึ่งทำให้ผู้ใช้ทั่วไปที่ไม่มีพื้นฐานด้านเทคโนโลยีสามารถใช้งานได้ทันที

**3. End-to-End MLOps Pipeline ที่พร้อม Production**
ระบบนี้ไม่ใช่แค่ Proof-of-Concept แต่มี:
- Experiment tracking ที่ audit ได้ผ่าน MLflow
- Containerized deployment ที่ reproducible
- Health check endpoint สำหรับ monitoring
- Graceful error handling ทั้งใน API และ Frontend

**4. เป้าหมาย SDG ที่วัดได้**
ระบบแสดงตัวเลข "ขยะที่ลดได้ (กก.)" โดยตรงในทุก prediction ทำให้ผู้ใช้เห็น impact ของการตัดสินใจที่ดีขึ้นได้ทันที ซึ่งสร้าง behavioral change ได้จริงมากกว่าระบบที่แค่แสดงตัวเลขพยากรณ์

**5. Zero Dependency on External AI Services**
โมเดลรันบน CPU ภายใน container เองทั้งหมด ไม่ต้องพึ่ง OpenAI API หรือ cloud ML services ไม่มีค่าใช้จ่าย per-request และข้อมูลไม่ถูกส่งออกนอกองค์กร เหมาะสำหรับองค์กรที่มีนโยบาย data privacy เข้มงวด

---

*รายงานฉบับนี้จัดทำขึ้นเพื่อประกอบโครงงาน MLOps วิชาเรียน*
*พัฒนาด้วย PyTorch · Prefect · MLflow · FastAPI · Streamlit · Docker*
*สนับสนุน SDG 2 (Zero Hunger) และ SDG 12 (Responsible Consumption)*

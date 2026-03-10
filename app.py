import os
import streamlit as st
import requests
from datetime import date

API_BASE = os.getenv("API_URL", "http://localhost:8000").rstrip("/predict")

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ระบบพยากรณ์ความต้องการอาหาร",
    page_icon="🍱",
    layout="centered",
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("ระบบพยากรณ์อาหาร")
    st.markdown("**ผู้พัฒนา:** Palus Kaewaram  \n**รหัสนักศึกษา:** 66070131")
    st.markdown("**ผู้คิดระบบและการทำงาน:** Natthapol Aiemburanont  \n**รหัสนักศึกษา:** 66070062")
    st.divider()
    st.subheader("SDG 12 — การบริโภคที่รับผิดชอบ")
    st.markdown(
        "ระบบนี้ช่วยให้เจ้าหน้าที่โรงอาหาร **พยากรณ์ความต้องการรายวัน** "
        "และเตรียมอาหารในปริมาณที่เหมาะสม เพื่อ**ลดขยะอาหาร** "
        "สอดคล้องกับ **เป้าหมายการพัฒนาที่ยั่งยืน SDG 12** ของสหประชาชาติ"
    )
    st.divider()
    st.caption("พัฒนาด้วย PyTorch · FastAPI · MLflow · Prefect")

# ── Fetch item list from API ──────────────────────────────────────────────────
ITEM_NAME_TH: dict[str, str] = {
    "Bread":          "ขนมปัง",
    "Brownie":        "บราวนี่",
    "Cake":           "เค้ก",
    "Coffee":         "กาแฟ",
    "Cookies":        "คุกกี้",
    "Hot chocolate":  "ช็อกโกแลตร้อน",
    "Medialuna":      "มีเดียลูนา (ครัวซอง)",
    "Pastry":         "เพสทรี่",
    "Sandwich":       "แซนด์วิช",
    "Tea":            "ชา",
}

ITEM_UNIT_TH: dict[str, str] = {
    "Bread":          "ก้อน",
    "Brownie":        "ชิ้น",
    "Cake":           "ชิ้น",
    "Coffee":         "แก้ว",
    "Cookies":        "ชิ้น",
    "Hot chocolate":  "แก้ว",
    "Medialuna":      "ชิ้น",
    "Pastry":         "ชิ้น",
    "Sandwich":       "ชิ้น",
    "Tea":            "แก้ว",
}

@st.cache_data(ttl=60)
def fetch_items() -> list[str]:
    try:
        resp = requests.get(f"{API_BASE}/items", timeout=3)
        resp.raise_for_status()
        return resp.json()["items"]
    except Exception:
        return list(ITEM_NAME_TH.keys())

items = fetch_items()
if not items:
    items = list(ITEM_NAME_TH.keys())

items_display = [f"{ITEM_NAME_TH.get(i, i)} ({i})" for i in items]
item_display_to_key = {f"{ITEM_NAME_TH.get(i, i)} ({i})": i for i in items}

# ── Main UI ───────────────────────────────────────────────────────────────────
st.title("🍱 ระบบพยากรณ์ความต้องการอาหารและวางแผนลดขยะ")
st.markdown("เลือกวันที่และรายการอาหาร เพื่อดูปริมาณที่ควรเตรียมและประมาณการขยะที่ลดได้")

col_date, col_item = st.columns([1, 1])
with col_date:
    selected_date = st.date_input("เลือกวันที่", value=date.today(), min_value=date(2024, 1, 1))
with col_item:
    selected_display = st.selectbox("เลือกรายการอาหาร", options=items_display)

if not selected_display:
    st.stop()

selected_item = item_display_to_key[selected_display]

if st.button("พยากรณ์ความต้องการ", type="primary", use_container_width=True):
    day_of_week = selected_date.weekday()
    is_weekend  = 1 if day_of_week >= 5 else 0

    with st.spinner("กำลังคำนวณ..."):
        try:
            resp = requests.get(
                f"{API_BASE}/predict",
                params={"day_of_week": day_of_week, "is_weekend": is_weekend, "item": selected_item},
                timeout=5,
            )
            resp.raise_for_status()
            data = resp.json()
        except requests.exceptions.ConnectionError:
            st.error("ไม่สามารถเชื่อมต่อ API ได้ กรุณาตรวจสอบว่า FastAPI กำลังทำงานที่พอร์ต 8000")
            st.stop()
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
            st.stop()

    # ── Result Cards ──────────────────────────────────────────────────────────
    day_names_th = ["วันจันทร์","วันอังคาร","วันพุธ","วันพฤหัสบดี","วันศุกร์","วันเสาร์","วันอาทิตย์"]
    item_th = ITEM_NAME_TH.get(selected_item, selected_item)
    unit    = ITEM_UNIT_TH.get(selected_item, "รายการ")
    st.success(f"ผลการพยากรณ์ **{item_th}** สำหรับ **{day_names_th[day_of_week]} ที่ {selected_date}**")

    col1, col2, col3 = st.columns(3)
    col1.metric(
        label="ยอดขายที่คาดการณ์",
        value=f"{data['predicted_demand']} {unit}",
        help="จำนวนที่คาดว่าจะขายได้ในวันนั้น คำนวณจากข้อมูลยอดขายจริงด้วย AI",
    )
    col2.metric(
        label="ปริมาณแนะนำให้เตรียม",
        value=f"{data['recommended_quantity']} {unit}",
        delta="+5% Safety Stock",
        help="จำนวนที่ควรเตรียม โดยบวก 5% เผื่อไว้เพื่อไม่ให้ขาด",
    )
    col3.metric(
        label="ขยะอาหารที่ลดได้",
        value=f"{data['waste_reduced_kg']} กก.",
        delta="เทียบกับการเตรียมเกิน",
        delta_color="inverse",
        help="น้ำหนักขยะอาหาร (กิโลกรัม) ที่ประหยัดได้เมื่อเทียบกับการเตรียมเผื่อมากเกินไป",
    )

    st.divider()
    with st.expander("ดูข้อมูล API Response"):
        st.json(data)

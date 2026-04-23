import streamlit as st

# إعدادات NutriX Pro (Purple Theme)
st.set_page_config(page_title="NutriX Pro", layout="centered")
st.markdown("<style>.main { background-color: #f3e5f5; } h1 { color: #4B0082; text-align: center; }</style>", unsafe_allow_html=True)

st.title("💜 NutriX Pro: عيادتك الذكية 🥗")
st.write("---")

# بيانات المريض
name = st.text_input("اسم المريض")
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("الوزن (كجم)", value=70.0)
    age = st.number_input("العمر", value=25)
with col2:
    gender = st.selectbox("الجنس", ["Female", "Male"])
    creatinine = st.number_input("الكرياتينين (للكلى)", value=1.0)

diagnosis = st.selectbox("الحالة الطبية", ["تغذية عامة", "مريض كلى (Renal)", "تكيس مبايض (PCOS/IR)", "قلب وضغط (Cardiac)"])

# محرك الحسابات الطبية
def calculate(w, a, g, d, cr):
    k = 0.7 if g == 'Female' else 0.9
    alpha = -0.329 if g == 'Female' else -0.411
    gfr = 141 * min(cr/k, 1)**alpha * max(cr/k, 1)**-1.209 * 0.993**a * (1.018 if g == 'Female' else 1.0)
    
    if d == "مريض كلى (Renal)": p_factor = 0.6 if gfr < 30 else 0.8
    elif d == "تكيس مبايض (PCOS/IR)": p_factor = 1.2
    else: p_factor = 1.0
    return int(gfr), int(w * p_factor)

if st.button("إصدار تقرير NutriX"):
    gfr_v, prot_v = calculate(weight, age, gender, diagnosis, creatinine)
    st.success(f"النتيجة: GFR = {gfr_v} | البروتين المطلوب = {prot_v} جرام")
    st.info("💡 جارٍ تجهيز جداول المعهد القومي للتغذية للبحث الشامل...")
  

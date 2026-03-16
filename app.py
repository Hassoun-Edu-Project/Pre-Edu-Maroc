import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hassoun-Edu-Project", layout="wide")

# 2. لمسات احترافية بالألوان (CSS)
st.markdown("""
    <style>
    .main { background-color: #fdfefe; }
    .stButton>button { 
        width: 100%; 
        border-radius: 25px; 
        background-color: #2e7d32; 
        color: white; 
        height: 3.5em;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        border: 2px solid #a5d6a7;
    }
    h1 { 
        color: #1e3d59; 
        text-align: center; 
        font-family: 'Cairo', sans-serif;
        padding: 20px;
        background: #e3f2fd;
        border-radius: 15px;
    }
    section[data-testid="stSidebar"] {
        background-color: #f1f8e9;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3976/3976625.png", width=120)
    st.title("Hassoun-Edu")
    st.markdown("---")
    st.header("🗂️ المحاور")
    choice = st.radio("انتقل إلى:", [
        "الرئيسية",
        "المذكرة اليومية",
        "القسم المشترك (Multiniveaux)",
        "مذكرة الأنشطة الموازية",
        "الجذاذات التربوية",
        "تقييم كفايات الأطفال",
        "التوزيعات السنوية"
    ])

# 4. محتوى الأقسام
st.title("🌟 منصة الوثائق التربوية")

if choice == "الرئيسية":
    st.subheader("مرحباً بكم في منصة Hassoun-Edu")
    st.info("فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي.")
    try:
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز", use_column_width=True)
    except:
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2 = st.columns(2)
    with col1:
        try:
            with open("document1.pdf", "rb") as f:
                st.download_button("📥 تحميل المذكرة (V1)", f, "daily_note_v1.pdf")
        except: st.error("الملف 1 غير متوفر")
    with col2:
        try:
            with open("cahier journal.arabe.pdf", "rb") as f:
                st.download_button("📥 تحميل المذكرة (بالعربية)", f, "cahier_journal_arabe.pdf")
        except: st.error("الملف العربي غير متوفر")

elif choice == "القسم المشترك (Multiniveaux)":
    st.subheader("👥 قسم القسم المشترك")
    try:
        with open("emploi_temps_multi.la rentrée scolaire.pdf", "rb") as f:
            st.download_button("📥 تحميل استعمال الزمن", f, "emploi_temps_multi.pdf")
    except: st.warning("يرجى رفع ملف القسم المشترك")

elif choice == "مذكرة الأنشطة الموازية":
    st.subheader("🎨 مذكرة الأنشطة الموازية")
    try:
        with open("fiche_pedagogique.pdf", "rb") as f:
            st.download_button("📥 تحميل الجذاذة", f, "fiche_activites_paralleles.pdf")
    except: st.warning("يرجى رفع ملف fiche_pedagogique.pdf")

elif choice == "الجذاذات التربوية":
    st.subheader("📝 قسم الجذاذات التربوية")
    try:
        with open("fiche_pedagogique.pdf", "rb") as f:
            st.download_button("📥 تحميل جذاذة النشاط", f, "fiche_pedagogique.pdf")
    except: st.warning("الملف غير متوفر")

elif choice == "تقييم كفايات الأطفال":
    st.subheader("📊 تقييم كفايات الأطفال")
    try:
        file_path = "Calendrier de mise en oeuvre de l'évaluation des compétences des enfants-Année scolaire 2025-2026.pdf"
        with open(file_path, "rb") as f:
            st.download_button("📥 تحميل جدولة التقييمات", f, "Calendrier_Evaluation.pdf")
    except: st.warning("يرجى رفع ملف التقييمات")

# --- دمج التوزيعات في صفحة واحدة ---
elif choice == "التوزيعات السنوية":
    st.subheader("🗓️ قسم التوزيعات السنوية")
    st.write("اختر نوع التوزيع الذي ترغب في تحميله:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📜 التوزيع السنوي العام")
        try:
            with open("distribution.pdf", "rb") as f:
                st.download_button("📥 تحميل التوزيع العام", f, "annual_plan.pdf")
        except: st.error("ملف distribution.pdf غير متوفر")
        
    with col2:
        st.markdown("### 📂 التوزيع الموضوعاتي")
        try:
            with open("distribution1.pdf", "rb") as f:
                st.download_button("📥 تحميل توزيع المشاريع", f, "distribution_thematique.pdf")
        except: st.error("ملف distribution1.pdf غير متوفر")

else:
    st.subheader(f"📂 {choice}")
    st.write("سيتم التزويد قريباً.")
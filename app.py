import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hassoun-Edu-Project", layout="wide")

# 2. لمسات احترافية بالألوان (CSS)
st.markdown("""
    <style>
    /* تغيير لون الخلفية العامة */
    .main { background-color: #fdfefe; }
    
    /* تنسيق الأزرار */
    .stButton>button { 
        width: 100%; 
        border-radius: 25px; 
        background-color: #2e7d32; /* أخضر تربوي */
        color: white; 
        height: 3.5em;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    
    /* تغيير لون الزر عند تمرير الفأرة */
    .stButton>button:hover {
        background-color: #1b5e20;
        border: 2px solid #a5d6a7;
    }

    /* تنسيق العنوان الرئيسي */
    h1 { 
        color: #1e3d59; 
        text-align: center; 
        font-family: 'Cairo', sans-serif;
        padding: 20px;
        background: #e3f2fd;
        border-radius: 15px;
    }
    
    /* تنسيق القائمة الجانبية */
    section[data-testid="stSidebar"] {
        background-color: #f1f8e9;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية مع الشعار
with st.sidebar:
    # إضافة شعار (يمكنكِ تغيير الرابط لاحقاً بشعارك الخاص)
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
        "التوزيعات السنوية",
        "جرد أنشطة المشاريع"
    ])

# 4. محتوى الأقسام (نفس الروابط التي نجحت معكِ)
st.title("🌟 منصة الوثائق التربوية")

if choice == "الرئيسية":
    st.subheader("مرحباً بكِ أستاذة عائشة")
    st.info("منصة متكاملة لدعم مربي التعليم الأولي بالمغرب.")
    st.image("https://img.freepik.com/free-vector/hand-drawn-back-school-background_23-2149031175.jpg", use_column_width=True)

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

elif choice == "الالقسم المشترك (Multiniveaux)":
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

else:
    st.subheader(f"📂 {choice}")
    st.write("هذا القسم سيتم تزويده بالوثائق قريباً.")
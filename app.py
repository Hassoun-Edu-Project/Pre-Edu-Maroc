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

# 3. القائمة الجانبية مع الشعار
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
        "التوزيعات السنوية",
        "جرد أنشطة المشاريع"
    ])

# 4. محتوى الأقسام
st.title("🌟 منصة الوثائق التربوية")

if choice == "الرئيسية":
    st.subheader("مرحباً بكم في منصة Hassoun-Edu")
    st.info("فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب.")
    st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", caption="بيئة تعليمية مبهجة للأطفال", use_column_width=True)
    st.markdown("---")
    st.write("هدفنا هو تيسير الوصول للوثائق التربوية لضمان جودة التعليم في مرحلة ما قبل التمدرس.")

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

# --- القسم الجديد الذي أضفناه هنا ---
elif choice == "الجذاذات التربوية":
    st.subheader("📝 قسم الجذاذات التربوية")
    st.info("يمكنكم تحميل نماذج الجذاذات التربوية من الروابط أدناه:")
    try:
        with open("fiche_pedagogique.pdf", "rb") as f: # استخدمت نفس اسم ملفك للتجربة
            st.download_button("📥 تحميل جذاذة النشاط", f, "fiche_pedagogique.pdf")
    except: 
        st.warning("يرجى رفع ملف الجذاذة (fiche_pedagogique.pdf) لتفعيل التحميل.")

elif choice == "التوزيعات السنوية":
    st.subheader("🗓️ قسم التوزيعات السنوية")
    try:
        with open("distribution.pdf", "rb") as file:
            st.download_button(
                label="تحميل التوزيع السنوي",
                data=file,
                file_name="annual_plan.pdf"
            )
    except FileNotFoundError:
        st.warning("تنبيه: هذا الملف غير موجود حالياً على GitHub.")

# هذا الجزء يظهر للأقسام المتبقية مثل (جرد أنشطة المشاريع)
else:
    st.subheader(f"📂 {choice}")
    st.write("هذا القسم سيتم تزويده بالوثائق قريباً.")
import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hassoun-Edu-Project", layout="wide")

# 2. تصميم الواجهة بالألوان
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #2e7d32; color: white; height: 3em; }
    h1 { color: #1e3d59; text-align: center; border-bottom: 2px solid #1e3d59; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 منصة Hassoun-Edu للوثائق التربوية")

# 3. القائمة الجانبية (هنا نضع كل المحاور)
with st.sidebar:
    st.header("القائمة الرئيسية")
    choice = st.radio("اختر المحور:", [
        "الرئيسية",
        "المذكرة اليومية",
        "القسم المشترك (Multiniveaux)",
        "مذكرة الأنشطة الموازية",
        "الجذاذات التربوية",
        "التوزيعات السنوية",
        "جرد أنشطة المشاريع"
    ])

# 4. محتوى الأقسام (الربط بين القائمة وما يظهر في الصفحة)

if choice == "الرئيسية":
    st.subheader("مرحباً بك الاستاذ محمد")
    st.info("هذه المنصة مخصصة لنشر الوثائق التربوية الخاصة بالتعليم الأولي بالمغرب.")
    st.write("استخدمي القائمة الجانبية للتنقل بين الأقسام وتحميل الوثائق.")

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2 = st.columns(2)
    with col1:
        try:
            with open("document1.pdf", "rb") as f:
                st.download_button("تحميل المذكرة (النسخة 1)", f, "daily_note_v1.pdf")
        except: st.error("الملف 1 غير متوفر")
    with col2:
        try:
            with open("cahier journal.arabe.pdf", "rb") as f:
                st.download_button("تحميل المذكرة (بالعربية)", f, "cahier_journal_arabe.pdf")
        except: st.error("الملف العربي غير متوفر")

elif choice == "الالقسم المشترك (Multiniveaux)":
    st.subheader("👥 قسم القسم المشترك")
    try:
        with open("emploi_temps_multi.la rentrée scolaire.pdf", "rb") as f:
            st.download_button("تحميل استعمال زمن القسم المشترك", f, "emploi_temps_multi.pdf")
    except: st.warning("يرجى رفع ملف القسم المشترك")

elif choice == "مذكرة الأنشطة الموازية":
    st.subheader("🎨 مذكرة وجذاذات الأنشطة الموازية")
    try:
        with open("fiche_pedagogique.pdf", "rb") as f:
            st.download_button("تحميل جذاذة الأنشطة الموازية", f, "fiche_activites_paralleles.pdf")
    except: st.warning("يرجى رفع ملف fiche_pedagogique.pdf")

else:
    # هذا الجزء يغطي بقية الأقسام التي لم نضع لها ملفات بعد
    st.subheader(f"📂 {choice}")
    st.write("سيتم تزويد هذا القسم بالوثائق قريباً.")
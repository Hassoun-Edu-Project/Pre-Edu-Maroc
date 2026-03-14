import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Hassoun-Edu-Project", layout="wide")

# تصميم الواجهة بالألوان
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #2e7d32; color: white; height: 3em; }
    .stRadio > label { font-weight: bold; color: #1565c0; font-size: 20px; }
    h1 { color: #1e3d59; text-align: center; border-bottom: 2px solid #1e3d59; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي للمنصة
st.title("📚 منصة Hassoun-Edu للوثائق التربوية")

# القائمة الجانبية (المحاور التي اقترحتِها)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3426/3426653.png", width=100) # أيقونة تعليمية
    st.header("القائمة الرئيسية")
    choice = st.radio("اختر المحور:", [
        "الرئيسية",
        "المذكرة اليومية",
        "استعمال الزمن",
        "القسم المشترك (Multiniveaux)",
        "الجذاذات التربوية",
        "أنشطة المشاريع التربوية",
        "التوزيعات السنوية"
    ])

# محتوى الأقسام بناءً على الاختيار
if choice == "الرئيسية":
    st.subheader("مرحباً بك استاذ محمد")
    st.info("هذه المنصة مخصصة لنشر الوثائق التربوية الخاصة بالتعليم الأولي بالمغرب.")
    st.write("استخدمي القائمة الجانبية للتنقل بين الأقسام وتحميل الوثائق المطلوبة.")

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    # زر التحميل للملف الذي رفعناه سابقاً
    try:
        with open("document1.pdf", "rb") as file:
            st.download_button(label="تحميل المذكرة اليومية (PDF)", data=file, file_name="daily_note.pdf")
    except:
        st.error("الملف غير متوفر حالياً.")

elif choice == "القسم المشترك (Multiniveaux)":
    st.subheader("👥 قسم القسم المشترك")
    st.write("يتضمن هذا القسم المذكرة اليومية واستعمال الزمن الخاص بالأقسام المشتركة.")
    # سنضيف أزرار التحميل هنا فور رفع ملفاتها

else:
    st.subheader(f"📂 {choice}")
    st.write("سيتم تزويد هذا القسم بالوثائق قريباً جداً.")
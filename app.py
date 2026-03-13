import streamlit as st

# إعدادات الصفحة والألوان
st.set_page_config(page_title="Hassoun-Edu-Project", layout="wide")

# إضافة لمسة جمالية بالألوان (CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; }
    h1 { color: #2E4053; text-align: center; font-family: 'Cairo', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.title("🌟 منصة Hassoun-Edu للوثائق التربوية")
st.write("---")

# القائمة الجانبية للتنظيم (Sidebar)
with st.sidebar:
    st.header("🗂️ المحاور التربوية")
    choice = st.radio("اختر القسم:", [
        "الرئيسية",
        "المذكرة اليومية",
        "استعمال الزمن (العادي / المشترك)",
        "الجذاذات التربوية",
        "مذكرة الأنشطة الموازية",
        "التوزيعات السنوية",
        "جرد أنشطة المشاريع"
    ])

# محتوى الصفحة بناءً على الاختيار
if choice == "الرئيسية":
    st.subheader("مرحباً بكِ في فضاء الأستاذ  محمد حسون")
    st.info("هذه المنصة مخصصة لدعم مربي التعليم الأولي بالمغرب عبر توفير وثائق تربوية جاهزة بجودة عالية.")
    st.image("https://via.placeholder.com/800x400.png?text=Educ-Pre-Maroc", use_column_width=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 المذكرة اليومية")
    st.write("هنا ستجدين المذكرات اليومية للقسم العادي والقسم المشترك.")
    # زر التحميل للمذكرة (الملف الذي رفعناه سابقاً)
    try:
        with open("document1.pdf", "rb") as file:
            st.download_button(label="تحميل المذكرة اليومية (PDF)", data=file, file_name="daily_notes.pdf")
    except FileNotFoundError:
        st.warning("الملف قيد التجهيز.. سيتم رفعه قريباً.")

elif choice == "استعمال الزمن (العادي / المشترك)":
    st.subheader("⏳ استعمال الزمن")
    st.write("نماذج متنوعة لاستعمالات الزمن.")
    # هنا يمكن إضافة أزرار تحميل لملفات أخرى لاحقاً

# ملاحظة: سنقوم بتفعيل بقية الأقسام فور تجهيز ملفاتها
else:
    st.subheader(f"قسم {choice}")
    st.write("هذا القسم سيتم تزويده بالوثائق قريباً جداً.")
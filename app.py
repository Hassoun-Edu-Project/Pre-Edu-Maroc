import streamlit as st
import os

# 1. إعدادات الصفحة والوصف
st.set_page_config(
    page_title="Hassoun-Edu | فضاء الوثائق التربوية", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Hassoun-Edu: فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب."
    }
)

# 2. التنسيق الجمالي (CSS) كما صممته سابقاً
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
    .trust-box {
        background-color: #e8f5e9; 
        padding: 15px; 
        border-radius: 10px; 
        border-right: 5px solid #2e7d32; 
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3976/3976625.png", width=120)
    st.title("Hassoun-Edu")
    st.markdown("---")
    st.header("🗂️ المحاور")
    choice = st.radio("انتقل إلى:", [
        "الرئيسية",
        "المذكرة اليومية",
        "استعمالات الزمن (Emploi du temps)",
        "المعينات الديداكتيكية (صور)", 
        "مذكرة الأنشطة الموازية",
        "الجذاذات التربوية",
        "تقييم كفايات الأطفال",
        "التوزيعات السنوية",
        "تواصل معنا"
    ])

# 4. محتوى الأقسام
st.title("🌟 منصة الوثائق التربوية")

if choice == "الرئيسية":
    st.subheader("مرحباً بكم في منصة Hassoun-Edu")
    st.markdown('<div class="trust-box"><p style="color: #2e7d32; font-size: 1.1em; font-weight: bold; margin: 0;">📢 فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب.</p></div>', unsafe_allow_html=True)
    try:
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز - الأستاذ محمد حسون", use_column_width=True)
    except:
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2, col3 = st.columns(3)
    
    # دالة مساعدة لتجنب تكرار الكود البرمجي (Helper function)
    def download_doc(file_path, button_label, download_name):
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button(button_label, f, download_name)
        else:
            st.error(f"الملف {file_path} غير موجود")

    with col1: download_doc("document1.pdf", "📥 المذكرة (V1)", "daily_note_v1.pdf")
    with col2: download_doc("cahier journal.arabe.pdf", "📥 المذكرة (بالعربية)", "daily_note_ar.pdf")
    with col3: download_doc("cahier journal.pdf", "📥 Cahier Journal (FR)", "cahier_journal_fr.pdf")

elif choice == "استعمالات الزمن (Emploi du temps)":
    st.subheader("🕒 قسم استعمالات الزمن")
    if os.path.exists("takayof.pdf"):
        with open("takayof.pdf", "rb") as f:
            st.download_button("📥 تحميل برنامج أسبوع الاستئناس", f, "takayof_adaptation.pdf")
    else:
        st.warning("يرجى رفع ملف takayof.pdf على السيرفر")

# ... (بقية الأقسام تتبع نفس المنطق القديم)
elif choice == "تواصل معنا":
    st.subheader("📧 يسعدنا التواصل معكم")
    contact_form = f"""
    <form action="https://formsubmit.co/hassoun.mohamed993@gmail.com" method="POST">
         <input type="text" name="name" placeholder="اسمك الكامل" required style="width:100%; margin-bottom:10px; border-radius:5px; border:1px solid #ccc; padding:10px;">
         <input type="email" name="email" placeholder="بريدك الإلكتروني" required style="width:100%; margin-bottom:10px; border-radius:5px; border:1px solid #ccc; padding:10px;">
         <textarea name="message" placeholder="اكتب اقتراحك هنا" style="width:100%; margin-bottom:10px; border-radius:5px; border:1px solid #ccc; padding:10px;" rows="4"></textarea>
         <button type="submit" style="background-color:#2e7d32; color:white; border:none; padding:12px 25px; border-radius:25px; cursor:pointer; width:100%; font-weight:bold;">إرسال</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
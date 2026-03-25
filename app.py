import streamlit as st
import os

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Hassoun-Edu | فضاء الوثائق التربوية", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إعدادات الأمان وكلمة المرور
ADMIN_PASSWORD = "youghrtamassinanas1993" 

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def logout():
    st.session_state['logged_in'] = False
    st.rerun()

# 3. تعريف الدوال الأساسية
def display_educational_img(img_name, caption):
    """دالة عرض وتحميل الصور"""
    if os.path.exists(img_name):
        st.image(img_name, caption=caption, use_column_width=True)
        with open(img_name, "rb") as f:
            st.download_button(f"تحميل {caption}", f, img_name, key=img_name)
    else:
        all_files = os.listdir('.')
        found = [f for f in all_files if img_name.lower() in f.lower()]
        if found:
            st.image(found[0], caption=caption, use_column_width=True)
        else:
            st.warning(f"⚠️ {caption} غير متوفرة")

# 4. التنسيق الجمالي (CSS)
st.markdown("""
    <style>
    .main { background-color: #fdfefe; }
    .stButton>button { 
        width: 100%; border-radius: 25px; background-color: #2e7d32; 
        color: white; height: 3.5em; font-weight: bold; border: none;
    }
    .stButton>button:hover { background-color: #1b5e20; }
    h1 { color: #1e3d59; text-align: center; background: #e3f2fd; border-radius: 15px; padding: 20px; }
    .trust-box { background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-right: 5px solid #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# 5. القائمة الجانبية ونظام الدخول
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3976/3976625.png", width=100)
    st.title("Hassoun-Edu")
    
    # خيار التنقل الرئيسي
    choice = st.radio("انتقل إلى:", [
        "الرئيسية", "المذكرة اليومية", "استعمالات الزمن (Emploi du temps)",
        "المعينات الديداكتيكية (صور)", "مذكرة الأنشطة الموازية",
        "الجذاذات التربوية", "تقييم كفايات الأطفال", "التوزيعات السنوية", "تواصل معنا"
    ])

    st.markdown("---")
    # نظام الدخول للمشرف
    if not st.session_state['logged_in']:
        st.subheader("🔐 منطقة المشرف")
        pwd = st.text_input("كلمة المرور", type="password")
        if st.button("دخول"):
            if pwd == ADMIN_PASSWORD:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("خطأ!")
    else:
        st.success("✅ وضع المشرف نشط")
        if st.button("تسجيل الخروج"):
            logout()

# 6. لوحة التحكم (تظهر فقط عند تسجيل الدخول)
if st.session_state['logged_in']:
    with st.expander("🛠️ لوحة رفع الملفات السريعة"):
        uploaded_file = st.file_uploader("ارفع ملفاً لاستبدال القديم أو إضافة جديد", type=['pdf', 'jpg', 'png', 'jpeg'])
        if uploaded_file is not None:
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"تم رفع {uploaded_file.name} بنجاح!")

# 7. محتوى الأقسام (المنطق الأصلي الخاص بك)
st.title("🌟 منصة الوثائق التربوية")

if choice == "الرئيسية":
    st.subheader("مرحباً بكم في منصة Hassoun-Edu")
    st.markdown('<div class="trust-box"><p>📢 فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب.</p></div>', unsafe_allow_html=True)
    try:
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز - الأستاذ محمد حسون", use_column_width=True)
    except:
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2, col3 = st.columns(3)
    # نستخدم try/except كما في كودك الأصلي لضمان الاستقرار
    with col1:
        try:
            with open("document1.pdf", "rb") as f: st.download_button("📥 المذكرة (V1)", f, "daily_note_v1.pdf")
        except: st.error("V1 غير متوفرة")
    # ... وباقي الأقسام كما هي في كودك ...
    with col2:
        try:
            with open("cahier journal.arabe.pdf", "rb") as f: st.download_button("📥 المذكرة (بالعربية)", f, "daily_note_ar.pdf")
        except: st.error("العربية غير متوفرة")
    with col3:
        try:
            with open("cahier journal.pdf", "rb") as f: st.download_button("📥 Cahier Journal (FR)", f, "cahier_journal_fr.pdf")
        except: st.error("الفرنسية غير متوفرة")

elif choice == "استعمالات الزمن (Emploi du temps)":
    st.subheader("🕒 قسم استعمالات الزمن")
    try:
        with open("takayof.pdf", "rb") as f: st.download_button("📥 تحميل برنامج أسبوع الاستئناس", f, "takayof_adaptation.pdf")
    except: st.warning("ملف takayof.pdf غير موجود")

elif choice == "المعينات الديداكتيكية (صور)":
    st.subheader("🖼️ قسم المعينات الديداكتيكية")
    tab1, tab2, tab3 = st.tabs(["🚦 التربية الطرقية", "🕌 الأعياد الدينية", "🇲🇦 الأعياد الوطنية"])
    with tab2:
        st.success("🌙 معرض صور شهر رمضان المبارك")
        c1, c2, c3 = st.columns(3)
        with c1: display_educational_img("ramadan_1.jpg", "زينة رمضان")
        with c2: display_educational_img("ramadan_2.jpg", "فانوس رمضان")
        with c3: display_educational_img("ramadan_3.jpg", "بطاقة تهنئة")

# ... (تكملة الأقسام بنفس الطريقة) ...
elif choice == "مذكرة الأنشطة الموازية":
    try:
        with open("cahier journal_activites_paralleles.pdf", "rb") as f: st.download_button("📥 تحميل المذكرة", f, "paralleles.pdf")
    except: st.warning("الملف غير متوفر")

elif choice == "الجذاذات التربوية":
    try:
        with open("fiche_pedagogique.pdf", "rb") as f: st.download_button("📥 تحميل الجذاذة", f, "fiche.pdf")
    except: st.warning("الملف غير متوفر")

elif choice == "تقييم كفايات الأطفال":
    try:
        files = os.listdir('.')
        target = next((f for f in files if "Calendrier" in f), None)
        if target:
            with open(target, "rb") as f: st.download_button("📥 تحميل الجدولة", f, "Calendrier.pdf")
    except: st.error("خطأ في الملف")

elif choice == "التوزيعات السنوية":
    col1, col2 = st.columns(2)
    with col1:
        try:
            with open("distribution.pdf", "rb") as f: st.download_button("📥 تحميل التوزيع العام", f, "plan.pdf")
        except: st.error("غير متوفر")
    with col2:
        try:
            with open("distribution1.pdf", "rb") as f: st.download_button("📥 تحميل توزيع المشاريع", f, "projects.pdf")
        except: st.error("غير متوفر")

elif choice == "تواصل معنا":
    st.subheader("📧 يسعدنا التواصل معكم")
    contact_form = f"""
    <form action="https://formsubmit.co/hassoun.mohamed993@gmail.com" method="POST">
         <input type="text" name="name" placeholder="اسمك الكامل" required style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px;">
         <input type="email" name="email" placeholder="بريدك الإلكتروني" required style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px;">
         <textarea name="message" placeholder="اكتب اقتراحك هنا" style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px;" rows="4"></textarea>
         <button type="submit" style="background-color:#2e7d32; color:white; border:none; padding:12px; border-radius:25px; width:100%;">إرسال</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
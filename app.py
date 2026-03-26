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
# تأكد من وجود admin_password في Secrets على Streamlit Cloud
try:
    ADMIN_PASSWORD = st.secrets["admin_password"]
except:
    ADMIN_PASSWORD = "Hassoun_Default_2026"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def logout():
    st.session_state['logged_in'] = False
    st.rerun()

# 3. تعريف الدوال الأساسية
def display_educational_img(img_name, caption):
    """دالة عرض وتحميل الصور مع معالجة الأخطاء"""
    if os.path.exists(img_name):
        st.image(img_name, caption=caption, use_column_width=True)
        with open(img_name, "rb") as f:
            st.download_button(f"تحميل {caption}", f, img_name, key=f"btn_{img_name}")
    else:
        all_files = os.listdir('.')
        found = [f for f in all_files if img_name.lower() in f.lower()]
        if found:
            st.image(found[0], caption=caption, use_column_width=True)
        else:
            st.warning(f"⚠️ {caption} غير متوفرة")

# 4. التنسيق الجمالي المطور (CSS) - النسخة المصححة
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
    <style>
    /* تأكدي أن كل شيء هنا داخل علامات الـ style */
    * { font-family: 'Cairo', sans-serif; }
    .main { background-color: #f8f9fa; }
    
    .feature-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-top: 5px solid #2e7d32;
        text-align: center;
        transition: all 0.3s ease;
        margin-bottom: 20px;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    h1 { color: #1e3d59; text-align: center; background: #ffffff; border-radius: 15px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    
    .stButton>button { 
        width: 100%; border-radius: 25px; background: linear-gradient(135deg, #2e7d32 0%, #4caf50 100%);
        color: white; height: 3.5em; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(46,125,50,0.3); }
    
    .trust-box { background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-right: 5px solid #2e7d32; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)
# 5. القائمة الجانبية ونظام الدخول
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3976/3976625.png", width=100)
    st.title("Hassoun-Edu")
    st.markdown("---")
    
    choice = st.radio("🏠 القائمة الرئيسية:", [
        "الرئيسية", "المذكرة اليومية", "استعمالات الزمن (Emploi du temps)",
        "المعينات الديداكتيكية (صور)", "مذكرة الأنشطة الموازية",
        "الجذاذات التربوية", "تقييم كفايات الأطفال", "التوزيعات السنوية", "تواصل معنا"
    ])

    st.markdown("---")
    if not st.session_state['logged_in']:
        st.subheader("🔐 منطقة المشرف")
        pwd = st.text_input("كلمة المرور", type="password")
        if st.button("دخول"):
            if pwd == ADMIN_PASSWORD:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("كلمة المرور غير صحيحة")
    else:
        st.success("✅ وضع المشرف نشط")
        if st.button("تسجيل الخروج"):
            logout()

# 6. لوحة التحكم
if st.session_state['logged_in']:
    with st.expander("🛠️ لوحة الإدارة - رفع الملفات"):
        uploaded_file = st.file_uploader("اختر ملفاً (PDF أو صور)", type=['pdf', 'jpg', 'png', 'jpeg'])
        if uploaded_file is not None:
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"تم رفع {uploaded_file.name} بنجاح!")

# 7. محتوى الأقسام
st.markdown("<h1>🌟 منصة Hassoun-Edu للوثائق التربوية</h1>", unsafe_allow_html=True)

if choice == "الرئيسية":
    st.markdown('<div class="trust-box"><p style="margin:0; font-weight:bold; color:#2e7d32; text-align:center;">📢 فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب.</p></div>', unsafe_allow_html=True)
    
    # شبكة البطاقات التفاعلية
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown('<div class="feature-card"><h2>📅</h2><h4>المذكرات</h4><p>المذكرة اليومية والأنشطة الموازية جاهزة للتحميل</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="feature-card"><h2>🕒</h2><h4>التخطيط</h4><p>استعمالات الزمن والتوزيعات السنوية والموضوعاتية</p></div>', unsafe_allow_html=True)
    with col_c:
        st.markdown('<div class="feature-card"><h2>📊</h2><h4>التقييم</h4><p>أدوات وشبكات تقييم كفايات طفل التعليم الأولي</p></div>', unsafe_allow_html=True)

    st.divider()
    try:
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز - الأستاذ محمد حسون", use_column_width=True)
    except:
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            with open("document1.pdf", "rb") as f: st.download_button("📥 المذكرة (V1)", f, "daily_note_v1.pdf")
        except: st.error("نسخة V1 غير متوفرة")
    with col2:
        try:
            with open("cahier journal.arabe.pdf", "rb") as f: st.download_button("📥 المذكرة (بالعربية)", f, "daily_note_ar.pdf")
        except: st.error("النسخة العربية غير متوفرة")
    with col3:
        try:
            with open("cahier journal.pdf", "rb") as f: st.download_button("📥 Cahier Journal (FR)", f, "cahier_journal_fr.pdf")
        except: st.error("النسخة الفرنسية غير متوفرة")

elif choice == "استعمالات الزمن (Emploi du temps)":
    st.subheader("🕒 قسم استعمالات الزمن")
    try:
        with open("takayof.pdf", "rb") as f: st.download_button("📥 تحميل برنامج أسبوع الاستئناس", f, "takayof_adaptation.pdf")
    except: st.warning("ملف takayof.pdf غير موجود")
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 👥 القسم المشترك")
        try:
            with open("emploi_temps_multi.la rentrée scolaire.pdf", "rb") as f: st.download_button("📥 تحميل (Multi)", f, "emploi_multi.pdf")
        except: st.error("الملف غير متوفر")

elif choice == "المعينات الديداكتيكية (صور)":
    st.subheader("🖼️ قسم المعينات الديداكتيكية")
    tab1, tab2, tab3 = st.tabs(["🚦 التربية الطرقية", "🕌 الأعياد الدينية", "🇲🇦 الأعياد الوطنية"])
    with tab2:
        st.success("🌙 معرض صور شهر رمضان المبارك")
        c1, c2, c3 = st.columns(3)
        with c1: display_educational_img("ramadan_1.jpg", "زينة رمضان")
        with col2: display_educational_img("ramadan_2.jpg", "فانوس رمضان") # تصحيح صغير هنا col2 -> c2
        with col3: display_educational_img("ramadan_3.jpg", "بطاقة تهنئة") # تصحيح صغير هنا col3 -> c3

elif choice == "مذكرة الأنشطة الموازية":
    st.subheader("🎨 مذكرة الأنشطة الموازية")
    try:
        with open("cahier journal_activites_paralleles.pdf", "rb") as f: st.download_button("📥 تحميل المذكرة", f, "paralleles.pdf")
    except: st.warning("الملف غير متوفر")

elif choice == "الجذاذات التربوية":
    st.subheader("📝 قسم الجذاذات التربوية")
    try:
        with open("fiche_pedagogique.pdf", "rb") as f: st.download_button("📥 تحميل الجذاذة", f, "fiche.pdf")
    except: st.warning("الملف غير متوفر")

elif choice == "تقييم كفايات الأطفال":
    st.subheader("📊 تقييم كفايات الأطفال")
    try:
        files = os.listdir('.')
        target = next((f for f in files if "Calendrier" in f), None)
        if target:
            with open(target, "rb") as f: st.download_button("📥 تحميل الجدولة", f, "Calendrier.pdf")
        else: st.warning("الملف غير متوفر")
    except: st.error("حدث خطأ في الوصول للملف")

elif choice == "التوزيعات السنوية":
    st.subheader("🗓️ قسم التوزيعات السنوية")
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
         <input type="text" name="name" placeholder="اسمك الكامل" required style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px; border:1px solid #ccc;">
         <input type="email" name="email" placeholder="بريدك الإلكتروني" required style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px; border:1px solid #ccc;">
         <textarea name="message" placeholder="اكتب رسالتك هنا" style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px; border:1px solid #ccc;" rows="4"></textarea>
         <button type="submit" style="background-color:#2e7d32; color:white; border:none; padding:12px; border-radius:25px; width:100%; cursor:pointer; font-weight:bold;">إرسال</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
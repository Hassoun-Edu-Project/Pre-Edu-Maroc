import streamlit as st

# 1. إعدادات الصفحة والوصف عند المشاركة
st.set_page_config(
    page_title="Hassoun-Edu | فضاء الوثائق التربوية", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Hassoun-Edu: فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب."
    }
)

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
    st.success("✨ ملف جديد: أسبوع الاستئناس")
    try:
        with open("takayof.pdf", "rb") as f: st.download_button("📥 تحميل برنامج أسبوع الاستئناس", f, "takayof_adaptation.pdf")
    except: st.warning("يرجى رفع ملف takayof.pdf")
    
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 👥 القسم المشترك")
        try:
            with open("emploi_temps_multi.la rentrée scolaire.pdf", "rb") as f: st.download_button("📥 تحميل (Multi)", f, "emploi_multi.pdf")
        except: st.error("الملف غير متوفر")
    with c2: st.markdown("### 👶 التمهيدي الأول"); st.info("قريباً")
    with c3: st.markdown("### 👦 التمهيدي الثاني"); st.info("قريباً")

elif choice == "المعينات الديداكتيكية (صور)":
    st.subheader("🖼️ قسم المعينات الديداكتيكية")
    st.write("صور ووسائل بصرية جاهزة للاستعمال في أنشطة القسم:")
    
    tab1, tab2, tab3 = st.tabs(["🚦 التربية الطرقية", "🕌 الأعياد الدينية", "🇲🇦 الأعياد الوطنية"])
    
    with tab1:
        st.info("نماذج وصور خاصة بالسلامة الطرقية للأطفال")
        st.write("سيتم رفع الصور قريباً...")

    with tab2:
        st.success("🌙 معرض صور شهر رمضان المبارك")
        
        # دالة ذكية لعرض الصورة والتحقق من وجودها
        def display_educational_img(img_name, caption):
            if os.path.exists(img_name):
                st.image(img_name, caption=caption, use_column_width=True)
                with open(img_name, "rb") as f:
                    st.download_button(f"تحميل {caption}", f, img_name, key=img_name)
            else:
                # محاولة البحث عن الملف إذا كان هناك اختلاف بسيط في الاسم
                all_files = os.listdir('.')
                found = [f for f in all_files if img_name.lower() in f.lower()]
                if found:
                    st.image(found[0], caption=caption, use_column_width=True)
                else:
                    st.warning(f"⚠️ الصورة {img_name} غير متوفرة في المجلد")

        # عرض الصور في شبكة (Grid)
        col1, col2, col3 = st.columns(3)
        with col1: display_educational_img("ramadan_1.jpg", "زينة رمضان")
        with col2: display_educational_img("ramadan_2.jpg", "فانوس رمضان")
        with col3: display_educational_img("ramadan_3.jpg", "بطاقة تهنئة")
        
        col4, col5 = st.columns(2)
        with col4: display_educational_img("ramadan_4.jpg", "رمضان كريم")
        with col5: display_educational_img("ramadan_5.jpg", "نشاط للأطفال")

    with tab3:
        st.info("ملصقات وصور خاصة بالمناسبات الوطنية المغربية")
        st.write("سيتم رفع الصور قريباً...")
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
        with open("Calendrier de mise en oeuvre de l'évaluation des compétences des enfants-Année scolaire 2025-2026.pdf", "rb") as f:
            st.download_button("📥 تحميل الجدولة", f, "Calendrier.pdf")
    except: st.warning("الملف غير متوفر")

elif choice == "التوزيعات السنوية":
    st.subheader("🗓️ قسم التوزيعات السنوية")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📜 التوزيع السنوي")
        try:
            with open("distribution.pdf", "rb") as f: st.download_button("📥 تحميل التوزيع العام", f, "plan.pdf")
        except: st.error("غير متوفر")
    with col2:
        st.markdown("### 📂 التوزيع الموضوعاتي")
        try:
            with open("distribution1.pdf", "rb") as f: st.download_button("📥 تحميل توزيع المشاريع", f, "projects.pdf")
        except: st.error("غير متوفر")

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
    st.markdown(contact_form, unsafe_allow_html=True)
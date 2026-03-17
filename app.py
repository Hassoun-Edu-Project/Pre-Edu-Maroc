import streamlit as st

# 1. إعدادات الصفحة والوصف الذي يظهر عند مشاركة الرابط
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
        "القسم المشترك (Multiniveaux)",
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
    
    # العبارة الشارحة لتعزيز الموثوقية
    st.markdown("""
        <div class="trust-box">
            <p style="color: #2e7d32; font-size: 1.1em; font-weight: bold; margin: 0;">
                📢 فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب.
            </p>
        </div>
    """, unsafe_allow_html=True)

    try:
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز - الأستاذ محمد حسون", use_column_width=True)
    except:
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)
    
    st.markdown("---")
    st.write("هدفنا هو تيسير الوصول للوثائق التربوية لضمان جودة التعليم في مرحلة ما قبل التمدرس.")

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    st.info("اختر النسخة المطلوبة للتحميل:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            with open("document1.pdf", "rb") as f:
                st.download_button("📥 المذكرة (V1)", f, "daily_note_v1.pdf")
        except: st.error("نسخة V1 غير متوفرة")
    with col2:
        try:
            with open("cahier journal.arabe.pdf", "rb") as f:
                st.download_button("📥 المذكرة (بالعربية)", f, "daily_note_ar.pdf")
        except: st.error("النسخة العربية غير متوفرة")
    with col3:
        try:
            # النسخة الفرنسية الجديدة التي أضفتِها
            with open("cahier journal.pdf", "rb") as f:
                st.download_button("📥 Cahier Journal (FR)", f, "cahier_journal_fr.pdf")
        except: st.error("النسخة الفرنسية غير متوفرة")

elif choice == "القسم المشترك (Multiniveaux)":
    st.subheader("👥 قسم القسم المشترك")
    try:
        with open("emploi_temps_multi.la rentrée scolaire.pdf", "rb") as f:
            st.download_button("📥 تحميل استعمال الزمن", f, "emploi_temps_multi.pdf")
    except: st.warning("يرجى رفع ملف القسم المشترك")

elif choice == "مذكرة الأنشطة الموازية":
    st.subheader("🎨 مذكرة الأنشطة الموازية")
    try:
        with open("cahier journal_activites_paralleles.pdf", "rb") as f:
            st.download_button("📥 تحميل مذكرة الأنشطة", f, "cahier_journal_paralleles.pdf")
    except: st.warning("يرجى رفع ملف المذكرة الموازية")

elif choice == "الجذاذات التربوية":
    st.subheader("📝 قسم الجذاذات التربوية")
    try:
        with open("fiche_pedagogique.pdf", "rb") as f:
            st.download_button("📥 تحميل جذاذة النشاط", f, "fiche_pedagogique.pdf")
    except: st.warning("يرجى رفع ملف fiche_pedagogique.pdf")

elif choice == "تقييم كفايات الأطفال":
    st.subheader("📊 تقييم كفايات الأطفال")
    try:
        file_path = "Calendrier de mise en oeuvre de l'évaluation des compétences des enfants-Année scolaire 2025-2026.pdf"
        with open(file_path, "rb") as f:
            st.download_button("📥 تحميل جدولة التقييمات", f, "Calendrier_Evaluation.pdf")
    except: st.warning("يرجى رفع ملف التقييمات")

elif choice == "التوزيعات السنوية":
    st.subheader("🗓️ قسم التوزيعات السنوية")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📜 التوزيع السنوي العام")
        try:
            with open("distribution.pdf", "rb") as f:
                st.download_button("📥 تحميل التوزيع العام", f, "annual_plan.pdf")
        except: st.error("ملف التوزيع العام غير متوفر")
    with col2:
        st.markdown("### 📂 التوزيع الموضوعاتي")
        try:
            with open("distribution1.pdf", "rb") as f:
                st.download_button("📥 تحميل توزيع المشاريع", f, "distribution_thematique.pdf")
        except: st.error("ملف التوزيع الموضوعاتي غير متوفر")

elif choice == "تواصل معنا":
    st.subheader("📧 يسعدنا التواصل معكم")
    st.write("نرحب باقتراحاتكم لتطوير المنصة أو لطلب استشارات تربوية.")
    
    contact_form = f"""
    <form action="https://formsubmit.co/hassoun.mohamed993@gmail.com" method="POST">
         <input type="text" name="name" placeholder="اسمك الكامل" required style="width:100%; margin-bottom:10px; border-radius:5px; border:1px solid #ccc; padding:10px;">
         <input type="email" name="email" placeholder="بريدك الإلكتروني" required style="width:100%; margin-bottom:10px; border-radius:5px; border:1px solid #ccc; padding:10px;">
         <textarea name="message" placeholder="اكتب اقتراحك هنا" style="width:100%; margin-bottom:10px; border-radius:5px; border:1px solid #ccc; padding:10px;" rows="4"></textarea>
         <button type="submit" style="background-color:#2e7d32; color:white; border:none; padding:12px 25px; border-radius:25px; cursor:pointer; width:100%; font-weight:bold;">إرسال</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
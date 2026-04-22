# 6. المحتوى الرئيسي
st.markdown(f"<div class='main-header'><h1>🌟 منصة Hassoun-Edu التربوية</h1></div>", unsafe_allow_html=True)

if choice == "الرئيسية":
    st.info("📢 فضاء مخصص لمربيات ومربي التعليم الأولي بالمغرب (FMPS).")
    if os.path.exists("fmps_classroom.jpg"):
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز - الأستاذ محمد حسون", use_column_width=True)
    else:
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)
        st.warning("⚠️ برجاء رفع صورة الواجهة باسم fmps_classroom.jpg من لوحة الإدارة")
    st.markdown("<p style='text-align:center; font-weight:bold; color:#1e3d59;'>مرحباً بكِ في فضائكِ التربوي المتميز</p>", unsafe_allow_html=True)

elif choice == "مقالات ومستجدات":
    st.markdown("<h2 style='text-align: center; color: #2e7d32;'>📑 ركن المقالات والمعرفة القانونية والتربوية</h2>", unsafe_allow_html=True)
    st.write("---")

    # المقال الأول
    st.markdown("""
    <div class='article-box'>
        <h3>📚 مرجعيات التعليم الأولي في المغرب: الرؤية والمسار</h3>
        تستمد هذه المرحلة قوتها من مرجعيات أساسية رسمت معالم "مدرسة الجودة":
        <h4>1. المرجعية الدستورية والخطب الملكية</h4>
        يعد <b>دستور 2011</b> المرجع الأسمى، إضافة إلى الرسالة الملكية السامية (يوليو 2018).
        <h4>2. المرجعية القانونية: القانون الإطار 51.17</h4>
        نصت المادة 8 منه على إلزامية التعليم الأولي بالنسبة للدولة والأسر.
    </div>
    """, unsafe_allow_html=True)

    # المقال الثاني
    st.markdown("""
    <div class='article-box'>
        <h3>🧩 المقاربات والمجالات التعلمية (المنهاج المغربي)</h3>
        تعتمد هندسة التعلمات على ستة مجالات متكاملة:
        <br><b>1. استكشاف الذات والمحيط</b> | <b>2. بناء أدوات تنظيم التفكير</b> | <b>3. التعبير اللغوي والتواصل</b>
        <br><b>4. تنمية الذوق الفني والجمالي</b> | <b>5. تنمية السلوك الحس حركي والرياضي</b> | <b>6. قيم وقواعد العيش المشترك</b>.
    </div>
    """, unsafe_allow_html=True)

    # المقال الثالث
    st.markdown("""
    <div class='article-box'>
        <h3>🎭 تقنيات التنشيط الحديثة</h3>
        <h4>1. لعب الأدوار (Jeu de Rôle):</h4> تمثيل أدوار مجتمعية لتطوير الشخصية والذكاء العاطفي.
        <h4>2. الأركان التربوية (Coins Pédagogiques):</h4> تقسيم الفضاء إلى أركان متخصصة تسمح بالتعلم الذاتي.
        <h4>3. العصف الذهني والسرد القصصي:</h4> تقنيات لتحفيز الإبداع وتطوير الرصيد اللغوي.
    </div>
    """, unsafe_allow_html=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    c1, c2, c3 = st.columns(3)
    with c1: display_resource("document1.pdf", "المذكرة V1")
    with c2: display_resource("cahier journal.arabe.pdf", "المذكرة بالعربية")
    with c3: display_resource("cahier journal.pdf", "Cahier Journal")

elif choice == "استعمالات الزمن":
    st.subheader("🕒 الجدولة الزمنية")
    display_resource("takayof.pdf", "برنامج أسبوع الاستئناس")

elif choice == "المعينات الديداكتيكية (صور)":
    st.markdown("<h2 style='text-align: center; color: #2e7d32;'>🖼️ مكتبة الوسائل التعليمية</h2>", unsafe_allow_html=True)
    t_logos, t_houses, t_nature = st.tabs(["🏷️ الشعارات", "🏡 المنازل", "🦋 الطبيعة"])
    
    with t_logos:
        col1, col2 = st.columns(2)
        with col1: display_resource("logo_spring_ar.png", "لوغو الربيع")
        with col2: display_resource("logo_spring_fr.png", "Logo")
            
    with t_houses:
        col1, col2, col3 = st.columns(3)
        with col1: display_resource("house_1.jpg", "منزل 1")
        with col2: display_resource("house_2.jpg", "منزل 2")
        with col3: display_resource("house_3.jpg", "منزل 3")
            
    with t_nature:
        col1, col2 = st.columns(2)
        with col1: display_resource("spring_flowers_1.jpg", "أزهار 1")
        with col2: display_resource("spring_flowers_2.jpg", "أزهار 2")

elif choice == "الجذاذات التربوية":
    st.subheader("📝 بنك الجذاذات (PDF)")
    display_resource("fiche_printemps.pdf", "جذاذة فصل الربيع")

elif choice == "تواصل معنا":
    st.success("📧 للتواصل: hassoun.mohamed993@gmail.com")
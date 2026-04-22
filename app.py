elif choice == "المعينات الديداكتيكية (صور)":
    st.markdown("<h2 style='text-align: center; color: #2e7d32;'>🖼️ مكتبة الوسائل التعليمية</h2>", unsafe_allow_html=True)
    t_logos, t_houses, t_nature = st.tabs(["🏷️ الشعارات", "🏡 المنازل", "🦋 الطبيعة"])
    
    with t_logos:
        c1, c2 = st.columns(2)
        with c1: 
            display_resource("logo_spring_ar.png", "لوغو الربيع")
        with c2: 
            display_resource("logo_spring_fr.png", "Logo")
            
    with t_houses:
        c1, c2, c3 = st.columns(3)
        with c1: 
            display_resource("house_1.jpg", "منزل 1")
        with c2: 
            display_resource("house_2.jpg", "منزل 2")
        with c3: 
            display_resource("house_3.jpg", "منزل 3")
            
    with t_nature:
        c1, c2 = st.columns(2)
        with c1: 
            display_resource("spring_flowers_1.jpg", "أزهار 1")
        with c2: 
            display_resource("spring_flowers_2.jpg", "أزهار 2")
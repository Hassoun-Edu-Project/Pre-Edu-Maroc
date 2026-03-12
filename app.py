import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(page_title="مكتبة الوثائق التربوية", page_icon="🏫")

st.title("📂 منصة الوثائق التربوية للتعليم الأولي")
st.markdown("---")

# 2. ذاكرة الموقع (Session State)
if 'edu_docs' not in st.session_state:
    st.session_state.edu_docs = []

# 3. القائمة الجانبية (Sidebar)
st.sidebar.header("📝 إضافة وثيقة جديدة")

doc_type = st.sidebar.selectbox("نوع الوثيقة:", [
    "استعمال الزمن", "المذكرة اليومية", "مذكرة الانشطة الموازية", 
    "جدادة الانشطة الموازية", "التوزيع السنوي", "جرد أنشطة المشاريع الموضوعتية"
])

level = st.sidebar.radio("المستوى:", [
    "المستوى الأول تمهيدي", "المستوى الثاني تمهيدي", "القسم المشترك (Multiniveaux)"
])

uploaded_file = st.sidebar.file_uploader("ارفع الوثيقة (PDF)", type=["pdf"])

if st.sidebar.button("نشر الوثيقة"):
    if uploaded_file:
        new_doc = {
            "نوع الوثيقة": "📄 " + doc_type,
            "المستوى": level,
            "اسم الملف": uploaded_file.name,
            "الملف الفعلي": uploaded_file.getvalue() # حفظ محتوى الملف للتحميل لاحقاً
        }
        st.session_state.edu_docs.append(new_doc)
        st.sidebar.success(f"تمت إضافة {doc_type} بنجاح!")
    else:
        st.sidebar.warning("يرجى رفع الملف أولاً")

# 4. عرض المحتوى (مرة واحدة فقط وبشكل منظم)
if st.session_state.edu_docs:
    st.subheader("📑 قائمة الوثائق المرفوعة")
    df_edu = pd.DataFrame(st.session_state.edu_docs)
    
    # عرض الجدول (بدون عمود 'الملف الفعلي' لأنه بيانات ثنائية لا تظهر في الجدول)
    st.dataframe(df_edu[["نوع الوثيقة", "المستوى", "اسم الملف"]], use_container_width=True)
    
    st.divider()
    
    # 5. منطقة الفلترة والتحميل
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📥 منطقة التحميل")
    with col2:
        selected_level = st.selectbox("تصفية حسب المستوى:", ["الكل", "المستوى الأول تمهيدي", "المستوى الثاني تمهيدي", "القسم المشترك (Multiniveaux)"])

    # عرض أزرار التحميل بناءً على التصفية
    for doc in st.session_state.edu_docs:
        if selected_level == "الكل" or doc['المستوى'] == selected_level:
            button_label = f"تحميل: {doc['نوع الوثيقة']} ({doc['المستوى']})"
            st.download_button(
                label=button_label,
                data=doc['الملف الفعلي'], # هنا نستخدم الملف الحقيقي الذي رفعه المستخدم
                file_name=doc['اسم الملف'],
                key=doc['اسم الملف'] + doc['المستوى']
            )
else:
    st.info("المكتبة التربوية فارغة. يرجى رفع الملفات من القائمة الجانبية.")
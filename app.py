import streamlit as st

st.set_page_config(page_title="Hassoun-Edu-Project", layout="centered")

st.title("منصة التعليم الأولي بالمغرب 🇲🇦")
st.write("مرحباً بكِ أستاذة عائشة في منصتك التربوية.")

# هذا هو الكود المسؤول عن زر التنزيل
try:
    with open("document1.pdf", "rb") as file:
        st.download_button(
            label="تنزيل الوثيقة التربوية (PDF)",
            data=file,
            file_name="document1.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("ملف الوثيقة غير موجود حالياً، يرجى التأكد من رفعه على GitHub.")

st.info("سيتم إضافة المزيد من الموارد التربوية قريباً.")
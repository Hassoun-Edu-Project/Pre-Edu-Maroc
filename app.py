import streamlit as st
import os

# --- إعدادات الصفحة (نفس إعداداتك السابقة) ---
st.set_page_config(page_title="Hassoun-Edu", layout="wide")

# --- دالة ذكية للتحميل (Fonction de téléchargement) ---
def smart_download_button(label, file_path, download_name):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            st.download_button(label, f, download_name)
    else:
        st.error(f"⚠️ {label} غير متوفر حالياً")

# --- القائمة الجانبية ---
with st.sidebar:
    st.title("Hassoun-Edu")
    choice = st.radio("انتقل إلى:", ["الرئيسية", "المذكرة اليومية", "استعمالات الزمن", "المعينات الديداكتيكية"])

# --- محتوى الأقسام ---
if choice == "الرئيسية":
    st.title("🌟 منصة الوثائق التربوية")
    st.info("مرحباً بك أستاذ محمد، المنصة جاهزة للعمل.")

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2 = st.columns(2)
    
    with col1:
        smart_download_button("📥 المذكرة بالعربية", "cahier_ar.pdf", "daily_ar.pdf")
    with col2:
        smart_download_button("📥 Cahier Journal (FR)", "cahier_fr.pdf", "daily_fr.pdf")

elif choice == "المعينات الديداكتيكية":
    st.subheader("🖼️ معرض الصور الذكي")
    # تحويل الصور إلى قائمة لتسهيل عرضها
    images_list = [
        {"path": "ramadan_1.jpg", "cap": "زينة رمضان"},
        {"path": "ramadan_2.jpg", "cap": "فانوس رمضان"},
        {"path": "ramadan_3.jpg", "cap": "بطاقة تهنئة"}
    ]
    
    cols = st.columns(3)
    for i, img in enumerate(images_list):
        with cols[i % 3]:
            if os.path.exists(img["path"]):
                st.image(img["path"], caption=img["cap"])
                with open(img["path"], "rb") as f:
                    st.download_button(f"تحميل {img['cap']}", f, img["path"], key=i)
            else:
                st.warning(f"قيد الرفع: {img['cap']}")
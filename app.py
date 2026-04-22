import streamlit as st
import os, requests, base64

# 1. الإعدادات والتنسيق
st.set_page_config(page_title="Hassoun-Edu", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
    * { font-family: 'Cairo', sans-serif; }
    .main-header { text-align: center; color: #1e3d59; background: white; padding: 20px; border-bottom: 5px solid #2e7d32; }
    .article-box { background: white; padding: 20px; border-right: 5px solid #2e7d32; border-radius: 10px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); line-height: 1.8; }
</style>
""", unsafe_allow_html=True)

# 2. الدوال الأساسية
def display_resource(file_name, caption):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            st.download_button(f"📥 تحميل {caption}", f, file_name, key=file_name)
    else:
        st.info(f"📍 {caption}")

# 3. القائمة الجانبية
with st.sidebar:
    st.title("Hassoun-Edu")
    choice = st.radio("🏠 القائمة:", ["الرئيسية", "مقالات ومستجدات", "المذكرة اليومية", "استعمالات الزمن", "المعينات الديداكتيكية", "تواصل معنا"])

st.markdown("<div class='main-header'><h1>🌟 منصة Hassoun-Edu التربوية</h1></div>", unsafe_allow_html=True)

# 4. المحتوى
if choice == "الرئيسية":
    st.info("📢 فضاء مخصص لمربيات ومربي التعليم الأولي بالمغرب (FMPS).")
    st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)

elif choice == "مقالات ومستجدات":
    st.markdown("## 📑 ركن المعرفة القانونية والتربوية")
    st.markdown("""
    <div class='article-box'>
        <h3>📚 مرجعيات التعليم الأولي في المغرب</h3>
        نصت المادة 8 من <b>القانون الإطار 51.17</b> على إلزامية التعليم الأولي ودمجه في التعليم الابتدائي.
    </div>
    <div class='article-box'>
        <h3>🧩 المجالات التعلمية الستة</h3>
        1. استكشاف الذات والمحيط | 2. تنظيم التفكير | 3. التعبير اللغوي | 4. الذوق الفني | 5. السلوك الحس حركي | 6. قيم العيش المشترك.
    </div>
    """, unsafe_allow_html=True)

elif choice == "المذكرة اليومية":
    col1, col2 = st.columns(2)
    with col1: display_resource("cahier_journal_ar.pdf", "المذكرة بالعربية")
    with col2: display_resource("cahier_journal_fr.pdf", "Cahier Journal")

elif choice == "استعمالات الزمن":
    display_resource("takayof.pdf", "برنامج أسبوع الاستئناس")

elif choice == "المعينات الديداكتيكية":
    t1, t2 = st.tabs(["🖼️ صور", "📝 جذاذات"])
    with t1:
        c1, c2 = st.columns(2)
        with c1: display_resource("spring_1.jpg", "صورة الربيع 1")
        with c2: display_resource("spring_2.jpg", "صورة الربيع 2")
    with t2:
        display_resource("fiche_pedagogique.pdf", "الجذاذة التربوية")

elif choice == "تواصل معنا":
    st.success("📧 للتواصل: hassoun.mohamed993@gmail.com")
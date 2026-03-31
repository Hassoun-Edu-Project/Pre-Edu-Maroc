import streamlit as st
import os
import requests
import base64

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Hassoun-Edu | فضاء الوثائق التربوية", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- دالة الرفع المطورة إلى GitHub ---
def upload_to_github(file_bytes, file_name):
    try:
        token = st.secrets["github_token"]
        repo = st.secrets["github_repo"]
        url = f"https://api.github.com/repos/{repo}/contents/{file_name}"
        headers = {"Authorization": f"token {token}", "Content-Type": "application/json"}
        
        get_response = requests.get(url, headers=headers)
        sha = get_response.json().get("sha") if get_response.status_code == 200 else None
        
        base64_content = base64.b64encode(file_bytes).decode("utf-8")
        data = {"message": f"تحديث/إضافة: {file_name}", "content": base64_content}
        if sha: data["sha"] = sha
            
        response = requests.put(url, headers=headers, json=data)
        return response.status_code
    except Exception as e:
        return str(e)

# 2. إعدادات الأمان
ADMIN_PASSWORD = st.secrets.get("admin_password", "Hassoun_Default_2026")
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False

# 3. دالة ذكية للتعامل مع الملفات (صور أو PDF)
def display_resource(file_name, caption):
    if os.path.exists(file_name):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            st.image(file_name, caption=caption, use_column_width=True)
        with open(file_name, "rb") as f:
            st.download_button(f"📥 تحميل {caption}", f, file_name, key=f"btn_{file_name}")
    else:
        st.info(f"📍 {caption} (باسم {file_name})")

# 4. التنسيق الجمالي (CSS)
st.markdown("""
<style>
    * { font-family: 'Cairo', sans-serif !important; }
    .stApp { background-color: #f8f9fa; }
    .main-header { color: #1e3d59; text-align: center; background: white; border-radius: 15px; padding: 20px; border-bottom: 5px solid #2e7d32; }
    .stButton>button { width: 100%; border-radius: 25px; background: linear-gradient(135deg, #2e7d32 0%, #4caf50 100%); color: white; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 5. القائمة الجانبية
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3976/3976625.png", width=80)
    st.title("Hassoun-Edu")
    choice = st.radio("🏠 القائمة الرئيسية:", ["الرئيسية", "المذكرة اليومية", "استعمالات الزمن", "المعينات الديداكتيكية (صور)", "الجذاذات التربوية", "تواصل معنا"])
    
    st.markdown("---")
    if not st.session_state['logged_in']:
        pwd = st.text_input("🔐 كلمة المرور", type="password")
        if st.button("دخول المشرف"):
            if pwd == ADMIN_PASSWORD:
                st.session_state['logged_in'] = True
                st.rerun()
    else:
        st.success("✅ وضع المشرف نشط")
        with st.expander("📤 رفع الوسائل/الوثائق"):
            up_files = st.file_uploader("اختر الملفات", accept_multiple_files=True)
            if up_files and st.button("🚀 بدء الرفع"):
                for f in up_files:
                    res = upload_to_github(f.getvalue(), f.name)
                    if res in [200, 201]: st.toast(f"تم رفع {f.name} ✅")
                st.balloons()
        if st.button("تسجيل الخروج"):
            st.session_state['logged_in'] = False
            st.rerun()

# 6. المحتوى
st.markdown(f"<div class='main-header'><h1>🌟 منصة Hassoun-Edu التربوية</h1></div>", unsafe_allow_html=True)

if choice == "الرئيسية":
    st.info("📢 فضاء مخصص لمربيات ومربي التعليم الأولي بالمغرب (FMPS).")
    
    # محاولة عرض صورتكِ الخاصة أولاً
    if os.path.exists("fmps_classroom.jpg"):
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز - الأستاذ محمد حسون", use_column_width=True)
    else:
        # صورة احتياطية في حال لم يتم رفع الصورة بعد
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)
        st.warning("⚠️ برجاء رفع صورة الواجهة باسم fmps_classroom.jpg من لوحة الإدارة")

    st.markdown("<p style='text-align:center; font-weight:bold; color:#1e3d59;'>مرحباً بكِ في فضائكِ التربوي المتميز</p>", unsafe_allow_html=True)

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
    st.markdown("<h2 style='text-align: center; color: #2e7d32;'>🖼️ مكتبة الوسائل التعليمية - فصل الربيع</h2>", unsafe_allow_html=True)
    t_logos, t_houses, t_nature = st.tabs(["🏷️ الشعارات", "🏡 المنازل للتلوين", "🦋 الفراشات والأزهار"])
    
    with t_logos:
        c1, c2 = st.columns(2)
        with c1: display_resource("logo_spring_ar.png", "لوغو الربيع (عربي)")
        with c2: display_resource("logo_spring_fr.png", "Logo Printemps")

    with t_houses:
        c1, c2, c3 = st.columns(3)
        with c1: display_resource("house_1.jpg", "تلوين منزل الربيع 1")
        with c2: display_resource("house_2.jpg", "تلوين منزل الربيع 2")
        with c3: display_resource("house_3.jpg", "تلوين منزل الربيع 3")

    with t_nature:
        c1, c2 = st.columns(2)
        with c1: display_resource("spring_flowers_1.jpg", "أزهار وفراشات 1")
        with c2: display_resource("spring_flowers_2.jpg", "أزهار وفراشات 2")
        c3, c4 = st.columns(2)
        with c3: display_resource("spring_flowers_3.jpg", "أزهار وفراشات 3")
        with c4: display_resource("spring_flowers_4.jpg", "أزهار وفراشات 4")

elif choice == "الجذاذات التربوية":
    st.subheader("📝 بنك الجذاذات (PDF)")
    display_resource("fiche_printemps.pdf", "جذاذة أنشطة فصل الربيع")

elif choice == "تواصل معنا":
    st.success("📧 للتواصل: hassoun.mohamed993@gmail.com")
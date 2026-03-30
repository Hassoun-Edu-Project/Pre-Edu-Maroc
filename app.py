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

# --- الدالة المطورة للرفع إلى GitHub (تعالج الخطأ 422) ---
def upload_to_github(file_bytes, file_name):
    try:
        token = st.secrets["github_token"]
        repo = st.secrets["github_repo"]
        url = f"https://api.github.com/repos/{repo}/contents/{file_name}"
        
        headers = {
            "Authorization": f"token {token}",
            "Content-Type": "application/json"
        }

        # الخطوة أ: التأكد إذا كان الملف موجوداً مسبقاً لجلب الـ SHA (بصمة الملف)
        get_response = requests.get(url, headers=headers)
        sha = None
        if get_response.status_code == 200:
            sha = get_response.json().get("sha")

        # الخطوة ب: تجهيز محتوى الملف
        base64_content = base64.b64encode(file_bytes).decode("utf-8")
        
        data = {
            "message": f"تحديث/إضافة وثيقة: {file_name}",
            "content": base64_content
        }
        
        # إذا وجدنا SHA، نضيفه للبيانات ليقوم GitHub بالتحديث بدل الرفض
        if sha:
            data["sha"] = sha
        
        # الخطوة ج: إرسال طلب الرفع النهائي
        response = requests.put(url, headers=headers, json=data)
        return response.status_code
    except Exception as e:
        return f"Error: {str(e)}"

# 2. إعدادات الأمان
try:
    ADMIN_PASSWORD = st.secrets["admin_password"]
except:
    ADMIN_PASSWORD = "Hassoun_Default_2026"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def logout():
    st.session_state['logged_in'] = False
    st.rerun()

# 3. الدوال المساعدة للعرض
def display_educational_img(img_name, caption):
    if os.path.exists(img_name):
        st.image(img_name, caption=caption, use_column_width=True)
        with open(img_name, "rb") as f:
            st.download_button(f"تحميل {caption}", f, img_name, key=f"btn_{img_name}")
    else:
        st.info(f"📍 {caption} قيد التجهيز (ارفعي الملف باسم {img_name})")

# 4. التنسيق الجمالي (CSS)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
<style>
    * { font-family: 'Cairo', sans-serif !important; }
    .stApp { background-color: #f8f9fa; }
    .feature-card {
        background-color: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #2e7d32;
        text-align: center; transition: all 0.3s ease; margin-bottom: 20px;
    }
    h1 { color: #1e3d59; text-align: center; background: white; border-radius: 15px; padding: 20px; }
    .stButton>button { 
        width: 100% !important; border-radius: 25px !important; 
        background: linear-gradient(135deg, #2e7d32 0%, #4caf50 100%) !important;
        color: white !important; font-weight: bold !important;
    }
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
        with st.expander("🛠️ رفع ملفات دائم (GitHub)"):
            up_file = st.file_uploader("اختر ملفاً", type=['pdf', 'jpg', 'png', 'jpeg'])
            if up_file:
                if st.button("🚀 تأكيد الرفع/التحديث"):
                    with st.spinner("جاري المزامنة مع المستودع..."):
                        status = upload_to_github(up_file.getvalue(), up_file.name)
                        if status in [200, 201]:
                            st.success(f"✅ تم الرفع/التحديث بنجاح!")
                            st.balloons()
                        else:
                            st.error(f"❌ خطأ تقني: {status}")
        
        if st.button("تسجيل الخروج"):
            logout()

# 6. محتوى الأقسام
st.markdown("<h1>🌟 منصة Hassoun-Edu للوثائق التربوية</h1>", unsafe_allow_html=True)

if choice == "الرئيسية":
    st.info("📢 فضاء تربوي مخصص لمربيات التعليم الأولي بالمغرب (FMPS).")
    col_a, col_b, col_c = st.columns(3)
    with col_a: st.markdown('<div class="feature-card"><h2>📅</h2><h4>المذكرات</h4></div>', unsafe_allow_html=True)
    with col_b: st.markdown('<div class="feature-card"><h2>🕒</h2><h4>التخطيط</h4></div>', unsafe_allow_html=True)
    with col_c: st.markdown('<div class="feature-card"><h2>📊</h2><h4>التقييم</h4></div>', unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2, col3 = st.columns(3)
    files = [("V1", "document1.pdf"), ("العربية", "cahier journal.arabe.pdf"), ("Français", "cahier journal.pdf")]
    for i, (label, fname) in enumerate(files):
        with [col1, col2, col3][i]:
            if os.path.exists(fname):
                with open(fname, "rb") as f: st.download_button(f"📥 تحميل {label}", f, fname)
            else: st.warning(f"📍 {label} غير متوفر (ارفعيه باسم {fname})")

elif choice == "استعمالات الزمن (Emploi du temps)":
    st.subheader("🕒 قسم استعمالات الزمن")
    if os.path.exists("takayof.pdf"):
        with open("takayof.pdf", "rb") as f: st.download_button("📥 تحميل برنامج أسبوع الاستئناس", f, "takayof.pdf")
    else: st.warning("📍 ملف takayof.pdf غير متوفر حالياً")

elif choice == "المعينات الديداكتيكية (صور)":
    st.subheader("🖼️ قسم المعينات الديداكتيكية")
    tab1, tab2 = st.tabs(["🚦 التربية الطرقية", "🕌 الأعياد"])
    with tab2:
        c1, c2, c3 = st.columns(3)
        with c1: display_educational_img("ramadan_1.jpg", "زينة رمضان")
        with c2: display_educational_img("ramadan_2.jpg", "فانوس رمضان")
        with c3: display_educational_img("ramadan_3.jpg", "بطاقة تهنئة")

elif choice == "تواصل معنا":
    st.subheader("📧 يسعدنا التواصل معكم")
    st.write("ارسل استفسارك إلى: hassoun.mohamed993@gmail.com")
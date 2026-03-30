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

# --- دالة الرفع الاحترافية إلى GitHub ---
def upload_to_github(file_bytes, file_name):
    try:
        token = st.secrets["github_token"]
        repo = st.secrets["github_repo"]
        # سيتم رفع الملف إلى المسار الرئيسي في المستودع
        url = f"https://api.github.com/repos/{repo}/contents/{file_name}"
        
        headers = {
            "Authorization": f"token {token}",
            "Content-Type": "application/json"
        }
        
        base64_content = base64.b64encode(file_bytes).decode("utf-8")
        
        data = {
            "message": f"إضافة وثيقة تربوية: {file_name}",
            "content": base64_content
        }
        
        response = requests.put(url, headers=headers, json=data)
        return response.status_code
    except Exception as e:
        return str(e)

# 2. إعدادات الأمان وكلمة المرور
try:
    ADMIN_PASSWORD = st.secrets["admin_password"]
except:
    ADMIN_PASSWORD = "Hassoun_Default_2026"

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def logout():
    st.session_state['logged_in'] = False
    st.rerun()

# 3. تعريف الدوال الأساسية
def display_educational_img(img_name, caption):
    """دالة عرض وتحميل الصور مع معالجة الأخطاء"""
    if os.path.exists(img_name):
        st.image(img_name, caption=caption, use_column_width=True)
        with open(img_name, "rb") as f:
            st.download_button(f"تحميل {caption}", f, img_name, key=f"btn_{img_name}")
    else:
        st.warning(f"⚠️ {caption} سيتم توفيرها قريباً")

# 4. التنسيق الجمالي المطور (CSS)
css_code = """
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
<style>
    * { font-family: 'Cairo', sans-serif !important; }
    .stApp { background-color: #f8f9fa; }
    .feature-card {
        background-color: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #2e7d32;
        text-align: center; transition: all 0.3s ease; margin-bottom: 20px;
    }
    .feature-card:hover { transform: translateY(-10px); }
    h1 { color: #1e3d59; text-align: center; background: #ffffff; border-radius: 15px; padding: 20px; }
    .stButton>button { 
        width: 100% !important; border-radius: 25px !important; 
        background: linear-gradient(135deg, #2e7d32 0%, #4caf50 100%) !important;
        color: white !important; font-weight: bold !important; border: none !important;
    }
    .trust-box { background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-right: 5px solid #2e7d32; }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

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
        # لوحة الإدارة المدمجة للرفع الدائم
        with st.expander("🛠️ رفع ملفات دائم (GitHub)"):
            up_file = st.file_uploader("اختر ملفاً", type=['pdf', 'jpg', 'png', 'jpeg'])
            if up_file:
                if st.button("🚀 تأكيد الرفع إلى GitHub"):
                    with st.spinner("جاري المزامنة..."):
                        status = upload_to_github(up_file.getvalue(), up_file.name)
                        if status in [200, 201]:
                            st.success(f"✅ تم رفع {up_file.name} بنجاح!")
                            st.balloons()
                        else:
                            st.error(f"❌ خطأ في الرفع: {status}")
        
        if st.button("تسجيل الخروج"):
            logout()

# 7. محتوى الأقسام
st.markdown("<h1>🌟 منصة Hassoun-Edu للوثائق التربوية</h1>", unsafe_allow_html=True)

if choice == "الرئيسية":
    st.markdown('<div class="trust-box"><p style="margin:0; font-weight:bold; color:#2e7d32; text-align:center;">📢 فضاء تربوي مخصص لتقاسم الوثائق والدلائل الخاصة بمربي التعليم الأولي بالمغرب.</p></div>', unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown('<div class="feature-card"><h2>📅</h2><h4>المذكرات</h4><p>المذكرة اليومية والأنشطة الموازية جاهزة للتحميل</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="feature-card"><h2>🕒</h2><h4>التخطيط</h4><p>استعمالات الزمن والتوزيعات السنوية والموضوعاتية</p></div>', unsafe_allow_html=True)
    with col_c:
        st.markdown('<div class="feature-card"><h2>📊</h2><h4>التقييم</h4><p>أدوات وشبكات تقييم كفايات طفل التعليم الأولي</p></div>', unsafe_allow_html=True)

    st.divider()
    st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)

elif choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2, col3 = st.columns(3)
    # ملاحظة: يمكنكِ الآن رفع هذه الملفات عبر لوحة الإدارة وستعمل الأزرار تلقائياً إذا تطابقت الأسماء
    for i, (label, fname) in enumerate([("V1", "document1.pdf"), ("العربية", "cahier journal.arabe.pdf"), ("Français", "cahier journal.pdf")]):
        with [col1, col2, col3][i]:
            if os.path.exists(fname):
                with open(fname, "rb") as f: st.download_button(f"📥 تحميل {label}", f, fname)
            else: st.info(f"📍 نسخة {label} قيد التجهيز")

elif choice == "المعينات الديداكتيكية (صور)":
    st.subheader("🖼️ قسم المعينات الديداكتيكية")
    tab1, tab2, tab3 = st.tabs(["🚦 التربية الطرقية", "🕌 الأعياد الدينية", "🇲🇦 الأعياد الوطنية"])
    with tab2:
        st.success("🌙 معرض صور شهر رمضان المبارك")
        c1, c2, c3 = st.columns(3)
        with c1: display_educational_img("ramadan_1.jpg", "زينة رمضان")
        with c2: display_educational_img("ramadan_2.jpg", "فانوس رمضان")
        with c3: display_educational_img("ramadan_3.jpg", "بطاقة تهنئة")

elif choice == "الجذاذات التربوية":
    st.markdown("<h1>📝 بنك الجذاذات التربوية الموسمية</h1>", unsafe_allow_html=True)
    tab_spring, tab_olympics = st.tabs(["🌿 جذاذات فصل الربيع", "🏆 أولمبياد الطفل"])
    with tab_spring:
        st.markdown('<div class="trust-box"><b>الهدف:</b> تعرف الطفل على مظاهر فصل الربيع.</div>', unsafe_allow_html=True)
        display_educational_img("spring_lesson.jpg", "لوحة استكشاف الربيع")

elif choice == "تواصل معنا":
    st.subheader("📧 يسعدنا التواصل معكم")
    contact_form = """
    <form action="https://formsubmit.co/hassoun.mohamed993@gmail.com" method="POST">
         <input type="text" name="name" placeholder="اسمك الكامل" required style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px; border:1px solid #ccc;">
         <input type="email" name="email" placeholder="بريدك الإلكتروني" required style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px; border:1px solid #ccc;">
         <textarea name="message" placeholder="اكتب رسالتك هنا" style="width:100%; margin-bottom:10px; border-radius:5px; padding:10px; border:1px solid #ccc;" rows="4"></textarea>
         <button type="submit" style="background-color:#2e7d32; color:white; border:none; padding:12px; border-radius:25px; width:100%; cursor:pointer; font-weight:bold;">إرسال</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
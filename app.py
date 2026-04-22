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
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    * { font-family: 'Cairo', sans-serif !important; }
    .stApp { background-color: #f8f9fa; }
    .main-header { color: #1e3d59; text-align: center; background: white; border-radius: 15px; padding: 20px; border-bottom: 5px solid #2e7d32; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 25px; background: linear-gradient(135deg, #2e7d32 0%, #4caf50 100%); color: white; font-weight: bold; }
    .article-box { background: white; padding: 20px; border-right: 5px solid #2e7d32; border-radius: 10px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

# 5. القائمة الجانبية
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3976/3976625.png", width=80)
    st.title("Hassoun-Edu")
    # تحديث القائمة بإضافة خيار "مقالات ومستجدات"
    choice = st.radio("🏠 القائمة الرئيسية:", [
        "الرئيسية", 
        "مقالات ومستجدات", 
        "المذكرة اليومية", 
        "استعمالات الزمن", 
        "المعينات الديداكتيكية (صور)", 
        "الجذاذات التربوية", 
        "تواصل معنا"
    ])
    
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
    if os.path.exists("fmps_classroom.jpg"):
        st.image("fmps_classroom.jpg", caption="فضاء تربوي متميز - الأستاذ محمد حسون", use_column_width=True)
    else:
        st.image("https://img.freepik.com/free-vector/happy-kids-classroom-scene_1308-27158.jpg", use_column_width=True)
        st.warning("⚠️ برجاء رفع صورة الواجهة باسم fmps_classroom.jpg من لوحة الإدارة")
    st.markdown("<p style='text-align:center; font-weight:bold; color:#1e3d59;'>مرحباً بكِ في فضائكِ التربوي المتميز</p>", unsafe_allow_html=True)

elif choice == "مقالات ومستجدات":
    st.markdown("<h2 style='text-align: center; color: #2e7d32;'>📑 ركن المقالات والمعرفة القانونية</h2>", unsafe_allow_html=True)
    st.write("---")
    
# المقال الأول: مرجعيات التعليم الأولي
    with st.expander("📚 مرجعيات التعليم الأولي في المغرب"):
        st.markdown("""
        <div class='article-box'>
        <h3>مرجعيات التعليم الأولي في المغرب: الرؤية والمسار</h3>
        يعتبر التعليم الأولي في المملكة المغربية ورشاً وطنياً استراتيجياً، يهدف إلى إرساء نظام تربوي عادل ومنصف. وتستمد هذه المرحلة قوتها وتنظيمها من مرجعيات أساسية رسمت معالم "مدرسة الجودة":

        <h4>1. المرجعية الدستورية والخطب الملكية</h4>
        يعد <b>دستور 2011</b> المرجع الأسمى، حيث نص على الحق في التربية والتعليم كحق أساسي. كما شكلت الرسالة الملكية السامية الموجهة للمشاركين في "اليوم الوطني للتعليم الأولي" (يوليو 2018) منعطفاً حاسماً، حيث اعتبر جلالة الملك أن التعليم الأولي هو القاعدة الصلبة لأي إصلاح تربوي.

        <h4>2. المرجعية القانونية: القانون الإطار 51.17</h4>
        يعتبر <b>القانون الإطار رقم 51.17</b> الوثيقة القانونية الأكثر إلزامية، حيث نصت المادة 8 منه على إلزامية التعليم الأولي بالنسبة للدولة والأسر، ودمجه تدريجياً في التعليم الابتدائي ليشكل سلكاً تعليمياً منسجماً.

        <h4>3. المرجعية الاستراتيجية: الرؤية الاستراتيجية 2015-2030</h4>
        وضعت الرؤية الاستراتيجية "التعليم الأولي" كرافعة أولى للإصلاح تحت شعار "من أجل مدرسة الإنصاف والجودة والارتقاء"، مؤكدة على ضرورة تعميم تعليم أولي ذو جودة بمواصفات موحدة.

        <h4>4. المرجعية التربوية: الإطار المنهاجي الجديد</h4>
        أصدرت وزارة التربية الوطنية <b>الإطار المنهاجي الوطني للتعليم الأولي</b>، وهو الوثيقة التي تحدد المجالات التعلمية (تطوير المهارات، بناء أدوات التفكير، القيم...) والمقاربة البيداغوجية القائمة على اللعب والاكتشاف.
        </div>
        """, unsafe_allow_html=True)
        st.caption("تحرير: Hassoun-Edu | 2026")
# المقال الثاني المصحح: المقاربات والمجالات التعلمية
    with st.expander("🧩 المقاربات والمجالات التعلمية في التعليم الأولي"):
        st.markdown("""
        <div class='article-box'>
        <h3>المقاربات البيداغوجية والمجالات التعلمية الستة</h3>
        تعتمد هندسة التعلمات في التعليم الأولي المغربي على تنظيم دقيق يراعي نمو الطفل الشامل، وذلك من خلال ستة مجالات تعلمية متكاملة:

        <h4>المجالات التعلمية الستة (المنهاج المغربي):</h4>
        <ol>
            <li><b>استكشاف الذات والمحيط:</b> يهدف إلى مساعدة الطفل على التعرف على جسمه وحواسه، وفهم البيئة الطبيعية والاجتماعية من حوله.</li>
            <li><b>بناء أدوات تنظيم التفكير:</b> يركز على اكتساب المفاهيم الرياضية والمنطقية الأولية (العدد، الشكل، الفضاء، والزمن).</li>
            <li><b>التعبير اللغوي والتواصل:</b> تطوير القدرات الشفهية والتواصلية للطفل كتمهيد لتعلم القراءة والكتابة.</li>
            <li><b>تنمية الذوق الفني والجمالي:</b> من خلال الرسم، التشكيل، المسرح، والموسيقى لتطوير حس الإبداع.</li>
            <li><b>تنمية السلوك الحس حركي والرياضي:</b> التركيز على المهارات الحركية الدقيقة والكبرى وتوازن الجسم.</li>
            <li><b>قيم وقواعد العيش المشترك:</b> غرس القيم الدينية والوطنية وقواعد السلوك والتعامل مع الآخرين.</li>
        </ol>

        <h4>المقاربات البيداغوجية المعتمدة:</h4>
        <ul>
            <li><b>بيداغوجيا اللعب:</b> المحرك الأساسي لكل الأنشطة، حيث يعتبر اللعب وسيلة التعلم الأولى.</li>
            <li><b>المقاربة بالمشروع:</b> توحيد الأنشطة حول مشروع موضوعاتي (مثل: مشروع القرية والمدينة).</li>
            <li><b>البيداغوجيا الفارقية:</b> مراعاة وتيرة التعلم الخاصة بكل طفل على حدة.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.caption("تحرير: Hassoun-Edu | تحديث وفق الإطار المنهاجي الوطني")

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
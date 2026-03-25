import streamlit as st
import os

# دالة ذكية للتحقق والتحميل (لتفادي اختفاء الأزرار)
def smart_download(file_path, label, download_name):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            st.download_button(label, f, download_name)
    else:
        # إذا لم يجد الملف، سيظهر تنبيه باسم الملف المطلوب لكي تعرف أين الخلل
        st.error(f"⚠️ الملف غير متوفر: {file_path}")

# --- قسم المذكرة اليومية ---
if choice == "المذكرة اليومية":
    st.subheader("📁 قسم المذكرة اليومية")
    col1, col2, col3 = st.columns(3)
    with col1: smart_download("document1.pdf", "📥 المذكرة (V1)", "daily_note_v1.pdf")
    with col2: smart_download("cahier journal.arabe.pdf", "📥 المذكرة (بالعربية)", "daily_note_ar.pdf")
    with col3: smart_download("cahier journal.pdf", "📥 Cahier Journal (FR)", "cahier_journal_fr.pdf")

# --- قسم مذكرة الأنشطة الموازية ---
elif choice == "مذكرة الأنشطة الموازية":
    st.subheader("🎨 مذكرة الأنشطة الموازية")
    # التأكد من الاسم كما هو في GitHub: cahier journal_activites_paralleles.pdf
    smart_download("cahier journal_activites_paralleles.pdf", "📥 تحميل المذكرة", "paralleles.pdf")

# --- قسم الجذاذات التربوية ---
elif choice == "الجذاذات التربوية":
    st.subheader("📝 قسم الجذاذات التربوية")
    smart_download("fiche_pedagogique.pdf", "📥 تحميل الجذاذة", "fiche.pdf")

# --- قسم تقييم كفايات الأطفال ---
elif choice == "تقييم كفايات الأطفال":
    st.subheader("📊 تقييم كفايات الأطفال")
    filename = "Calendrier de mise en oeuvre de l'évaluation des compétences des enfants-Année scolaire 2025-2026.pdf"
    smart_download(filename, "📥 تحميل الجدولة", "Calendrier.pdf")

# --- قسم التوزيعات السنوية ---
elif choice == "التوزيعات السنوية":
    st.subheader("🗓️ قسم التوزيعات السنوية")
    col1, col2 = st.columns(2)
    with col1: smart_download("distribution.pdf", "📥 تحميل التوزيع العام", "plan.pdf")
    with col2: smart_download("distribution1.pdf", "📥 تحميل توزيع المشاريع", "projects.pdf")
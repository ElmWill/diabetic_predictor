import streamlit as st

st.set_page_config(page_title="Tips for Diabetes", page_icon="🩺", layout="wide")

st.markdown("""
<style>
body {
    background-color: #f7f9fc;
}

.tip-container {
    display: flex;
    flex-wrap: wrap;
    gap: 50px;
}

.tip-card {
    background-color: #E5E1DA;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    flex: 1 1 calc(45% - 20px);
    min-width: 300px;
    margin-bottom: 30px;
}

.tip-card h3 {
    color: #205781;
}

.tip-card ul {
    padding-left: 20px;
    margin-top: 10px;
}

.tip-card li {
    margin-bottom: 16px;
    font-size: 16px;
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

st.title("🩺 Tips for Managing Diabetes")

st.markdown("## ✨ Stay Healthy with These Simple Tips")

st.markdown('<div class="tip-container">', unsafe_allow_html=True)

def tip_card(title, tips):
    html = f'<div class="tip-card"><h3>{title}</h3><ul>'
    for tip in tips:
        html += f'<li>{tip}</li>'
    html += '</ul></div>'
    st.markdown(html, unsafe_allow_html=True)

tip_card("🥗 Healthy Eating", [
    "Focus on vegetables, fruits, lean proteins, and whole grains.",
    "Limit foods high in sugar.",
    "Eat smaller, more frequent meals."
])

tip_card("🏃 Regular Exercise", [
    "Find ways to be active throughout the day.",
    "Include walking, swimming, cycling, etc.",
    "Exercise improves insulin sensitivity."
])

tip_card("🩸 Blood Sugar Monitoring", [
    "Check blood sugar regularly.",
    "Maintain a record to track trends and adjust."
])

tip_card("💊 Medication Adherence", [
    "Take medicines as prescribed, even if you feel good.",
    "Don't change doses without consulting your doctor."
])

tip_card("🧘 Lifestyle Management", [
    "Avoid smoking and heavy drinking.",
    "Learn ways to manage stress.",
    "Get moving! Taking a walk can help you unwind.",
    "Get enough sleep."
])

tip_card("🏥 Regular Health Checkups", [
    "Visit your doctor for regular screening."
])

st.markdown('</div>', unsafe_allow_html=True)

st.success("🌟 Consistency is the key to managing diabetes successfully!")
st.caption("📝 Disclaimer: Always consult your healthcare provider for medical advice.")
st.caption("🔍 Source: https://www.cdc.gov/diabetes/living-with/index.html")
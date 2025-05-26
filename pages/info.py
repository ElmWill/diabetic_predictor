import streamlit as st

st.set_page_config(page_title="Information", page_icon="🩺", layout="wide")

st.markdown("""
<style>
body {
    background-color: #E5E1DA;
}

.info-container {
    display: flex;
    flex-wrap: wrap;
    gap: 50px;
}

.info-card {
    background-color: #E5E1DA;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    flex: 1 1 calc(45% - 20px);
    min-width: 300px;
    margin-bottom: 30px;
}

.info-card h3 {
    color: #205781;
}

.info-card ul {
    padding-left: 20px;
    margin-top: 10px;
}

.info-card li {
    margin-bottom: 16px;
    font-size: 16px;
    line-height: 2.0;
}

</style>
""", unsafe_allow_html=True)

st.title("💉 About Diabetes")

st.markdown("---")

st.markdown('<div class="info-container">', unsafe_allow_html=True)

def info_card(title, info):
    html = f'<div class="info-card"><h3>{title}</h3><ul>'
    for item in info:
        html += f'{item}'
    html += '</ul></div>'
    st.markdown(html, unsafe_allow_html=True)

info_card("🔍 What is Diabetes?", [
         """Diabetes is a condition that happens when your blood sugar (glucose) is too high. 
         It develops when your pancreas doesn't make enough insulin or any at all, or when your 
         body isn't responding to the effects of insulin properly. Diabetes affects people of all ages. 
         Most forms of diabetes are chronic (lifelong), and all forms are manageable with medications 
         and/or lifestyle changes.\n\n Glucose (sugar) mainly comes from carbohydrates in your food and drinks. It's your body's go-to 
         source of energy. Your blood carries glucose to all your body's cells to use for energy. When 
         glucose is in your bloodstream, it needs help — a “key” — to reach its final destination. This 
         key is insulin (a hormone). If your pancreas isn't making enough insulin or your body isn't 
         using it properly, glucose builds up in your bloodstream, causing high blood sugar (hyperglycemia).\n\nOver time, 
         having consistently high blood glucose can cause health problems, such as heart disease, 
         nerve damage and eye issues. The technical name for diabetes is diabetes mellitus. Another condition 
         shares the term “diabetes” — diabetes insipidus — but they're distinct. They share the name “diabetes” 
         because they both cause increased thirst and frequent urination. Diabetes insipidus is much rarer 
         than diabetes mellitus.
         """])

info_card("📋 How Common is Diabetes?", [
         """Diabetes is common. Approximately 37.3 million people in the United States have diabetes, which is about 11% of the population. 
            Type 2 diabetes is the most common form, representing 90% to 95% of all diabetes cases. About 537 million adults across the world 
            have diabetes. Experts predict this number will rise to 643 million by 2030 and 783 million by 2045.
            """])

info_card("🩸 What Causes Diabetes?", [
         """Too much glucose circulating in your bloodstream causes diabetes, regardless of the type. However, the reason why your blood 
         glucose levels are high differs depending on the type of diabetes. Causes of diabetes include:\n\n 1. Insulin resistance: Type 2 diabetes 
         mainly results from insulin resistance. Insulin resistance happens when cells in your muscles, fat and liver don't respond as they 
         should to insulin. Several factors and conditions contribute to varying degrees of insulin resistance, including obesity, lack of 
         physical activity, diet, hormonal imbalances, genetics and certain medications.\n\n 2. Autoimmune disease: Type 1 diabetes and LADA happen 
         when your immune system attacks the insulin-producing cells in your pancreas.\n\n 3. Hormonal imbalances: During pregnancy, the placenta 
         releases hormones that cause insulin resistance. You may develop gestational diabetes if your pancreas can't produce enough insulin 
         to overcome the insulin resistance. Other hormone-related conditions like acromegaly and Cushing syndrome can also cause Type 2 
         diabetes.\n\n 4. Pancreatic damage: Physical damage to your pancreas — from a condition, surgery or injury — can impact its ability to 
         make insulin, resulting in Type 3c diabetes.\n\n 5. Genetic mutations: Certain genetic mutations can cause MODY and neonatal diabetes.\n\n Long-term use of certain medications can also lead to Type 2 diabetes, including HIV/AIDS medications and corticosteroids.
         """])

# st.header("🔍 What is Diabetes?")
# st.markdown("""Diabetes is a condition that happens when your blood sugar (glucose) is too high. 
#          It develops when your pancreas doesn't make enough insulin or any at all, or when your 
#          body isn't responding to the effects of insulin properly. Diabetes affects people of all ages. 
#          Most forms of diabetes are chronic (lifelong), and all forms are manageable with medications 
#          and/or lifestyle changes.\n\n Glucose (sugar) mainly comes from carbohydrates in your food and drinks. It's your body's go-to 
#          source of energy. Your blood carries glucose to all your body's cells to use for energy. When 
#          glucose is in your bloodstream, it needs help — a “key” — to reach its final destination. This 
#          key is insulin (a hormone). If your pancreas isn't making enough insulin or your body isn't 
#          using it properly, glucose builds up in your bloodstream, causing high blood sugar (hyperglycemia).\n\n Over time, 
#          having consistently high blood glucose can cause health problems, such as heart disease, 
#          nerve damage and eye issues. The technical name for diabetes is diabetes mellitus. Another condition 
#          shares the term “diabetes” — diabetes insipidus — but they're distinct. They share the name “diabetes” 
#          because they both cause increased thirst and frequent urination. Diabetes insipidus is much rarer 
#          than diabetes mellitus.
#          """)

# st.header("📋 How Common is Diabetes?")
# st.markdown("""Diabetes is common. Approximately 37.3 million people in the United States have diabetes, which is about 11% of the population. 
#             Type 2 diabetes is the most common form, representing 90% to 95% of all diabetes cases. About 537 million adults across the world 
#             have diabetes. Experts predict this number will rise to 643 million by 2030 and 783 million by 2045.
#             """)

# st.header("🩸 What Causes Diabetes?")
# st.markdown("""Too much glucose circulating in your bloodstream causes diabetes, regardless of the type. However, the reason why your blood 
#          glucose levels are high differs depending on the type of diabetes. Causes of diabetes include:\n 1. Insulin resistance: Type 2 diabetes 
#          mainly results from insulin resistance. Insulin resistance happens when cells in your muscles, fat and liver don't respond as they 
#          should to insulin. Several factors and conditions contribute to varying degrees of insulin resistance, including obesity, lack of 
#          physical activity, diet, hormonal imbalances, genetics and certain medications.\n 2. Autoimmune disease: Type 1 diabetes and LADA happen 
#          when your immune system attacks the insulin-producing cells in your pancreas.\n 3. Hormonal imbalances: During pregnancy, the placenta 
#          releases hormones that cause insulin resistance. You may develop gestational diabetes if your pancreas can't produce enough insulin 
#          to overcome the insulin resistance. Other hormone-related conditions like acromegaly and Cushing syndrome can also cause Type 2 
#          diabetes.\n 4. Pancreatic damage: Physical damage to your pancreas — from a condition, surgery or injury — can impact its ability to 
#          make insulin, resulting in Type 3c diabetes.\n 5. Genetic mutations: Certain genetic mutations can cause MODY and neonatal diabetes.\n 
#          Long-term use of certain medications can also lead to Type 2 diabetes, including HIV/AIDS medications and corticosteroids.
#          """)

st.success("✨ Early detection and proper management are key to living a healthy life with diabetes.")
st.caption("📝 Source: https://my.clevelandclinic.org/health/diseases/7104-diabetes")
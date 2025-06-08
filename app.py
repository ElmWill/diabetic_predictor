import streamlit as st

main_page = st.Page(
    "pages/about.py",
    title="About Us",
    icon=":material/home:",
    default=True,
)

predictor = st.Page(
    "pages/diabetic_predictor_app.py",
    title="Diabetic Predictor App",
    icon=":material/calculate:",
)

info_page = st.Page(
    "pages/info.py",
    title="Information",
    icon=":material/info:",
)

tips_page = st.Page(
    "pages/tips.py",
    title="Tips",
    icon=":material/article:",
)

pg = st.navigation(pages=[main_page, predictor, info_page, tips_page])

pg.run()
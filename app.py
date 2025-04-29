import streamlit as st

main_page = st.Page(
    "pages/diabetic_predictor_app.py",
    title="Diabetic Predictor App",
    icon=":material/home:",
    default=True,
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

pg = st.navigation(pages=[main_page, info_page, tips_page])

pg.run()
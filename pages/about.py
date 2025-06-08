import streamlit as st

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
        body {
            background-color: #FAE7C9;
        }
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 30px;
        }
        .text-box {
            font-size: 16px;
            text-align: justify;
        }
        .image-style {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="title">About Us</div>', unsafe_allow_html=True)
# Spacer & Garis Pemisah
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# Logo ditampilkan di tengah
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 2, 1])
with col_logo_2:
    st.markdown(
        "<p style='text-align: center; font-size: 16px; font-style: italic; margin-top: 10px;'>"
        "Know the Risk. Take Control."
        "</p>",
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

image_url1 = "https://www.ekahospital.com/storage/gallery/1666942772-Diabetes-Melitus-(1).jpg"
image_url2 = "https://cdn.analyticsvidhya.com/wp-content/uploads/2022/01/Diabetes-Prediction-Using-Machine-Learning.webp"
image_url3 = "https://mandayahospitalgroup.com/wp-content/uploads/2024/05/diabetes.jpg"

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(
        f'<img src="{image_url1}" class="image-style">', unsafe_allow_html=True
    )
with col2:
    st.markdown(
        '<div class="text-box">'
        'PreDia is an innovative digital platform designed to help people detect diabetes risk early through an artificial intelligence-based approach. With the increasing prevalence of diabetes worldwide, we see the importance of a solution that can provide fast, accurate, and easily accessible risk predictions for anyone. PreDia is here as an answer to this need by combining user health data and intelligent algorithms to provide informative and personalized risk assessments. Simply by filling in some basic information about their body condition and lifestyle, users can get an initial picture of their possible risk of diabetes.'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns([2, 1])
with col3:
    st.markdown(
        '<div class="text-box">'
        'The main goal of PreDia is not only to provide prediction results, but also to increase public awareness of the importance of prevention and early detection. We believe that education and preventive measures are the main keys to reducing the number of diabetes sufferers. With information presented clearly and easily understood, PreDia encourages users to take positive steps, such as consulting with medical personnel, implementing a healthy diet, and exercising regularly. We also provide various educational resources that can help users better understand risk factors, early symptoms, and how to manage potential diabetes threats in everyday life.'
        '</div>',
        unsafe_allow_html=True
    )
with col4:
    st.markdown(
        f'<img src="{image_url2}" class="image-style">', unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

col5, col6 = st.columns([1, 2])
with col5:
    st.markdown(
        f'<img src="{image_url3}" class="image-style">', unsafe_allow_html=True
    )
with col6:
    st.markdown(
        '<div class="text-box">'
        'We developed PreDia with the principles of accuracy, reliability, and ease of use as top priorities. While our predictions do not replace a medical diagnosis, we are committed to continually improving our system to be a trusted early companion on the path to a healthier life. Through PreDia, we hope that every individual has a better chance to understand their health and take control of it early on.'
        '</div>',
        unsafe_allow_html=True
    )
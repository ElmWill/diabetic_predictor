import joblib
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="DiaPred", layout="wide")

# Custom CSS untuk styling
st.markdown("""
    <style>
    body {
        background-color: #FAE7C9;
    }
    .section-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .sub-title {
        text-align: center;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .input-box {
        background-color: #BDDDE4;
        padding: 15px 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .input-container {
        background-color: #BDDDE4;
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .predict-button {
        background-color: #BDDDE4;
        color: white;
        padding: 12px 24px;
        font-size: 22px;
        border-radius: 12px;
        text-align: center;
        border: none;
        width: 200px;
        font-weight: bold;
    }
    .predict-button:hover {
        background-color: #3d9499;
        cursor: pointer;
    }
        .result-box {
        background-color: #bfe3ee;
        color: #223a5f;
        padding: 15px;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        border-radius: 12px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

smoking_mapping = {
    "never": 0,
    "No Info": -1, 
    "current": 2,
    "former": 1
}

gender_mapping = {
    "Female": 0,
    "Male": 1
}

st.markdown('<div class="section-title">Diabetic Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Please fill in all sections...</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox('Gender', list(gender_mapping.keys()))
with col2:
    age = st.number_input('Age', min_value=0, max_value=120, value=30)

col3, col4 = st.columns(2)
with col3:
    smoking = st.selectbox('Smoking History', list(smoking_mapping.keys()))
with col4:
    hypertension_choice = st.selectbox('Hypertension', ['Yes', 'No'])
    hypertension = 1 if hypertension_choice == 'Yes' else 0

col5, col6 = st.columns(2)
with col5:
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0)
with col6:
    bp = st.number_input('Blood Pressure', min_value=50, max_value=200, value=120)

col7, col8 = st.columns(2)
with col7:
    hba1c = st.number_input('HbA1c Level', min_value=3.0, max_value=15.0, value=5.5, format="%.2f")
with col8:
    glucose = st.number_input('Glucose Level', min_value=50, max_value=300, value=100)

import os
import joblib

# Dapatkan path ke direktori file ini (pages/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Buat path absolut ke model dan scaler
model_path = os.path.join(current_dir, "diabetes_model.joblib")

# Load model dan scaler
model, scaler = joblib.load(open("pages/diabetes_model.joblib", "rb"))



centered_button = st.columns(3)[1]
with centered_button:
    predict_clicked = st.button("Predict", use_container_width=True)

if predict_clicked:
    input_data = np.array([[gender_mapping[gender], age, smoking_mapping[smoking],
                            hypertension, bmi, bp, hba1c, glucose]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    result = 'Diabetic' if prediction == 1 else 'Not Diabetic'

    st.markdown("### Prediction:")
    st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

    if prediction == 1:
        st.markdown("### Recommended Prescription:")
        st.write("💪🏻 Regular exercise (at least 30 mins per day)")
        st.write("🥗 Balanced diet (low sugar, high fiber)")
        st.write("💊 Medication as prescribed by a doctor (e.g., Metformin)")
    else:
        st.markdown("✨ Keep maintaining a healthy lifestyle!")

# st.markdown("""
#     <br><br>
#     <div style="text-align: center; font-weight: bold; font-size: 18px;">Contact us:</div>
#     <div style="text-align: center; margin-top: 10px;">
#         <img src="https://img.icons8.com/ios-filled/50/x.png" width="40" style="margin: 10px;"/>
#         <img src="https://img.icons8.com/ios-filled/50/instagram-new.png" width="40" style="margin: 10px;"/>
#         <img src="https://img.icons8.com/ios-filled/50/whatsapp.png" width="40" style="margin: 10px;"/>
#     </div>
# """, unsafe_allow_html=True)
    
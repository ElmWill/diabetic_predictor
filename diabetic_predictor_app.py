import pickle
import pandas as pd
import numpy as np
import streamlit as st

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

st.title('🩺 Diabetic Predictor App')

gender = st.selectbox('Gender', list(gender_mapping.keys()))
age = st.number_input('Age', min_value=0, max_value=120, value=30)
smoking = st.selectbox('Smoking History', list(smoking_mapping.keys()))
hypertension = st.selectbox('Hypertension', [0, 1])
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0)
bp = st.number_input('Blood Pressure', min_value=50, max_value=200, value=120)
hba1c = st.number_input('HbA1c Level', min_value=3.0, max_value=15.0, value=5.5)
glucose = st.number_input('Glucose Level', min_value=50, max_value=300, value=100)

with open('pages/diabetes_model.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

if st.button('Predict'):
    input_data = np.array([[gender_mapping[gender], age, smoking_mapping[smoking],hypertension, bmi, bp, hba1c, glucose]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    result = 'Diabetic' if prediction == 1 else 'Not Diabetic'
    
    st.write(f'### Prediction: {result}')
    
    # Prescription recommendations
    if prediction == 1:
        st.write("### Recommended Prescription:")
        st.write("💪🏻 Regular exercise (at least 30 mins per day)")
        st.write("🥗 Balanced diet (low sugar, high fiber)")
        st.write("💊 Medication as prescribed by a doctor (e.g., Metformin)")
    else:
        st.write("### ✨ Keep maintaining a healthy lifestyle!")
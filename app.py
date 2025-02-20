import pickle
import streamlit as st
st.set_page_config(page_title="Diabetes Prediction", layout="wide", page_icon="🧑‍⚕")
diabetes_model_path=r"C:\Users\pawan\OneDrive\Documents\Desktop\AIML\Logistic Regression\diabetes_model.sav"
diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))

st.title("Diabetes Prediction using ML")
col1, col2, col3 = st.columns(3)
with col1:
    pregnancies = st.text_input("Number of Pregnancies")
with col2:
    glucose = st.text_input("Glucose Level")
with col3:
    blood_pressure = st.text_input("Blood Pressure")
with col1:
    skin_thickness = st.text_input("Skin Thickness")
with col2:
    insulin = st.text_input("Insulin")
with col3:
    bmi = st.text_input("BMI")
with col1:
    dpf = st.text_input("Diabetes Pedigree Function")
with col2:
    age = st.text_input("Age")
with col3:
    submit = st.button("Predict")
    if submit:
        input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
        prediction = diabetes_model.predict([input_data])
        if prediction[0] == 1:
            st.error("You have Diabetes!")
        else:
            st.success("You don't have Diabetes!")        
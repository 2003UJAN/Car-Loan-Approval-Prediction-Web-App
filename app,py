import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("loan_approval_model.pkl")

st.set_page_config(page_title="Car Loan Approval Predictor")
st.title("🚗 Car Loan Approval Predictor")

# Input form
st.sidebar.header("Applicant Information")

def user_input():
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    married = st.sidebar.selectbox("Married", ["Yes", "No"])
    dependents = st.sidebar.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.sidebar.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.sidebar.selectbox("Self Employed", ["Yes", "No"])
    applicant_income = st.sidebar.slider("Applicant Income", 10000, 100000)
    coapplicant_income = st.sidebar.slider("Coapplicant Income", 0, 50000)
    loan_amount = st.sidebar.slider("Loan Amount", 500000, 3000000)
    loan_term = st.sidebar.selectbox("Loan Term (months)", [60, 120, 180, 240, 300, 360])
    credit_history = st.sidebar.selectbox("Credit History", [1, 0])
    property_area = st.sidebar.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])
    car_model = st.sidebar.selectbox("Car Model", ["Sedan", "Hatchback", "SUV", "Convertible", "Coupe", "Van", "Truck"])
    car_price = st.sidebar.slider("Car Price", 500000, 4000000)

    data = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history,
        'Property_Area': property_area,
        'Car_Model': car_model,
        'Car_Price': car_price
    }
    return pd.DataFrame([data])

input_df = user_input()

# Encode input
encoded_df = input_df.copy()
label_mappings = {
    'Gender': {'Male': 1, 'Female': 0},
    'Married': {'Yes': 1, 'No': 0},
    'Dependents': {'0': 0, '1': 1, '2': 2, '3+': 3},
    'Education': {'Graduate': 1, 'Not Graduate': 0},
    'Self_Employed': {'Yes': 1, 'No': 0},
    'Property_Area': {'Urban': 2, 'Rural': 0, 'Semiurban': 1},
    'Car_Model': {'Sedan': 0, 'Hatchback': 1, 'SUV': 2, 'Convertible': 3, 
                  'Coupe': 4, 'Van': 5, 'Truck': 6}
}
for col, mapping in label_mappings.items():
    encoded_df[col] = encoded_df[col].map(mapping)

# Predict
if st.button("Predict Loan Approval"):
    prediction = model.predict(encoded_df)[0]
    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Denied")


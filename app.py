import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("📊 Customer Churn Prediction App")
st.write("Enter customer details to check if they will churn.")

# Inputs
customer_id = st.text_input("Customer ID")

gender = st.selectbox("Gender", ["Male", "Female"])

# 🔥 REPLACED SeniorCitizen with AGE INPUT
age = st.number_input("Age", min_value=16, max_value=55, value=25)

partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
phoneservice = st.selectbox("Phone Service", ["Yes", "No"])

tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72)
monthly = st.number_input("Monthly Charges", min_value=10.0, max_value=200.0)
total = st.number_input("Total Charges", min_value=0.0, max_value=10000.0)

# Encoding function
def encode(val):
    return 1 if val == "Yes" else 0

gender_val = 1 if gender == "Male" else 0

# Prepare input row
input_data = pd.DataFrame({
    "CustomerID": [int(customer_id) if customer_id else 0],
    "Gender": [gender_val],
    "Age": [age],                     # 🔥 NEW AGE COLUMN
    "Partner": [encode(partner)],
    "Dependents": [encode(dependents)],
    "Tenure": [tenure],
    "PhoneService": [encode(phoneservice)],
    "MonthlyCharges": [monthly],
    "TotalCharges": [total]
})

# Predict
if st.button("Predict"):
    pred = model.predict(input_data)[0]
    if pred == 1:
        st.error("❌ Customer is likely to CHURN!")
    else:
        st.success("✅ Customer will STAY!")

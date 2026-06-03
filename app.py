import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("🏦 Loan Eligibility Predictor")

gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
married = st.selectbox("Married", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
education = st.selectbox("Education", [0, 1], format_func=lambda x: "Graduate" if x == 1 else "Not Graduate")
self_employed = st.selectbox("Self Employed", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
income = st.number_input("Applicant Income", min_value=0)
co_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Term (days)", [360, 120, 180, 240, 300, 480])
credit_history = st.selectbox("Credit History", [1, 0], format_func=lambda x: "Good" if x == 1 else "Bad")
property_area = st.selectbox("Property Area", [0, 1, 2], format_func=lambda x: ["Rural", "Semiurban", "Urban"][x])

if st.button("Check Eligibility"):
    features = np.array([[gender, married, dependents, education,
                          self_employed, income, co_income, loan_amount,
                          loan_term, credit_history, property_area]])
    result = model.predict(features)
    if result[0] == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected")
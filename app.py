import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="🏦",
    layout="centered"
)

st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            background-color: #1a56db;
            color: white;
            font-size: 1.1rem;
            padding: 0.75rem;
            border-radius: 10px;
            border: none;
            margin-top: 1rem;
        }
        .stButton>button:hover { background-color: #1e429f; }
        .result-box {
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            font-size: 1.4rem;
            font-weight: bold;
            margin-top: 1.5rem;
        }
        .approved { background-color: #def7ec; color: #03543f; border: 2px solid #0e9f6e; }
        .rejected { background-color: #fde8e8; color: #771d1d; border: 2px solid #f05252; }
        .section-header {
            font-size: 1rem;
            font-weight: 600;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin: 1.5rem 0 0.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

model = pickle.load(open('model.pkl', 'rb'))
model_columns = pickle.load(open('columns.pkl', 'rb'))

st.title("🏦 Loan Eligibility Predictor")
st.markdown("Fill in the applicant details below to check loan eligibility instantly.")
st.divider()

st.markdown('<p class="section-header">👤 Personal Information</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Dependents", [0, 1, 2, 3])
with col2:
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    age = st.number_input("Age", min_value=18, max_value=70, value=30)

st.markdown('<p class="section-header">💰 Financial Details</p>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    income = st.number_input("Applicant Income (₹/month)", min_value=0, step=1000, value=5000)
    co_income = st.number_input("Coapplicant Income (₹/month)", min_value=0, step=1000, value=0)
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=700)
with col4:
    loan_amount_full = st.number_input("Loan Amount (₹)", min_value=0, step=10, value=150)
    loan_amount = loan_amount_full / 1000
    loan_term = st.selectbox("Loan Term", [360, 120, 180, 240, 300, 480],
                              format_func=lambda x: f"{x} days")
    credit_history = st.selectbox("Credit History", ["Good", "Bad"])

st.markdown('<p class="section-header">🏡 Other Details</p>', unsafe_allow_html=True)
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

st.divider()

if st.button("Check Loan Eligibility →"):

    # Age validation
    if age < 21 or age > 60:
        st.error("❌ Applicant age must be between 21 and 60 years.")
        st.stop()

    # Credit score warning
    if credit_score < 650:
        st.warning("⚠️ Credit score below 650 significantly reduces approval chances.")

    # Encode inputs
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    education_val = 0 if education == "Graduate" else 1
    self_employed_val = 1 if self_employed == "Yes" else 0
    credit_val = 1 if credit_history == "Good" else 0
    property_val = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]

    # Engineered features
    total_income = income + co_income
    dti = loan_amount / (total_income + 1)
    emi = loan_amount / loan_term
    income_loan_ratio = total_income / (loan_amount + 1)

    # Build input in exact column order
    input_dict = {
        'Gender': gender_val,
        'Married': married_val,
        'Dependents': dependents,
        'Education': education_val,
        'Self_Employed': self_employed_val,
        'ApplicantIncome': income,
        'CoapplicantIncome': co_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_val,
        'Property_Area': property_val,
        'Total_Income': total_income,
        'DTI': dti,
        'EMI': emi,
        'Income_Loan_Ratio': income_loan_ratio
    }

    input_df = pd.DataFrame([input_dict])[model_columns]
    result = model.predict(input_df)

    if result[0] == 1:
        st.markdown('<div class="result-box approved">✅ Loan Approved! The applicant is eligible.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box rejected">❌ Loan Rejected. The applicant does not meet the criteria.</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Built with scikit-learn & Streamlit · First ML project by Srisha Jha")
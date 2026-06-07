import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="🏦",
    layout="centered"
)

st.markdown("""
    <style>
        .main { padding-top: 2rem; }
        .stButton>button {
            width: 100%;
            background-color: #1a56db;
            color: white;
            font-size: 1.1rem;
            padding: 0.75rem;
            border-radius: 10px;
            border: none;
            margin-top: 1rem;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #1e429f;
        }
        .result-box {
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            font-size: 1.4rem;
            font-weight: bold;
            margin-top: 1.5rem;
        }
        .approved {
            background-color: #def7ec;
            color: #03543f;
            border: 2px solid #0e9f6e;
        }
        .rejected {
            background-color: #fde8e8;
            color: #771d1d;
            border: 2px solid #f05252;
        }
        .section-header {
            font-size: 1rem;
            font-weight: 600;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin: 1.5rem 0 0.5rem 0;
        }
        div[data-testid="stSelectbox"] label,
        div[data-testid="stNumberInput"] label {
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

model = pickle.load(open('model.pkl', 'rb'))

st.title("🏦 Loan Eligibility Predictor")
st.markdown("Fill in the applicant details below to check loan eligibility instantly.")
st.divider()

st.markdown('<p class="section-header">👤 Personal Information</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
with col2:
    married = st.selectbox("Marital Status", ["Yes", "No"])

col3, col4 = st.columns(2)
with col3:
    dependents = st.selectbox("Number of Dependents", [0, 1, 2, 3])
with col4:
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])

self_employed = st.selectbox("Self Employed", ["Yes", "No"])

st.markdown('<p class="section-header">💰 Financial Details</p>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    income = st.number_input("Applicant Income (₹)", min_value=0, step=1000, value=5000)
with col6:
    co_income = st.number_input("Coapplicant Income (₹)", min_value=0, step=1000, value=0)

col7, col8 = st.columns(2)
with col7:
    loan_amount = st.number_input("Loan Amount (₹ thousands)", min_value=0, step=10, value=150)
with col8:
    loan_term = st.selectbox("Loan Term", [360, 120, 180, 240, 300, 480], format_func=lambda x: f"{x} days")

st.markdown('<p class="section-header">🏡 Other Details</p>', unsafe_allow_html=True)
col9, col10 = st.columns(2)
with col9:
    credit_history = st.selectbox("Credit History", ["Good", "Bad"])
with col10:
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

st.divider()

if st.button("Check Loan Eligibility →"):
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    education_val = 0 if education == "Graduate" else 1
    self_employed_val = 1 if self_employed == "Yes" else 0
    credit_val = 1 if credit_history == "Good" else 0
    property_val = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]

    features = np.array([[gender_val, married_val, dependents, education_val,
                          self_employed_val, income, co_income, loan_amount,
                          loan_term, credit_val, property_val]])

    result = model.predict(features)

    if result[0] == 1:
        st.markdown('<div class="result-box approved">✅ Loan Approved! The applicant is eligible.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box rejected">❌ Loan Rejected. The applicant does not meet the criteria.</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Built with scikit-learn & Streamlit · First ML project by Srisha Jha")

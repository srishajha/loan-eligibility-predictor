🏦 Loan Eligibility Predictor

A machine learning web app that predicts whether a loan application will be approved or rejected based on applicant details.

Live App: https://srisha-loan-eligibility-predictor.streamlit.app/

About the Project

Banks receive thousands of loan applications daily. This project automates the eligibility check using a Gradient Boosting classification model trained on real applicant data. It also applies real-world lending rules like age validation and credit score thresholds.


Tech Stack

- Python — core language
- pandas & numpy — data cleaning and processing
- scikit-learn — machine learning model
- Streamlit — web app interface
- Jupyter Notebook — exploratory data analysis


Model Performance

- Algorithm: Gradient Boosting Classifier
- Accuracy: 80% (improved from 76% Random Forest baseline)
- Dataset: Loan Prediction Dataset (Kaggle) — 614 rows, 12 columns

Engineered Features
- Total Income: applicant income + coapplicant income
- DTI Ratio: loan amount / total income (higher = riskier)
- EMI: loan amount / loan term (monthly repayment burden)
- Income Loan Ratio: total income / loan amount (higher = safer)

Real-World Rules Applied
- Age must be between 21 and 60 years
- Credit score below 650 triggers a warning

## How to Run Locally

1. Clone the repo
   git clone https://github.com/srishajha/loan-eligibility-predictor.git

2. Install dependencies
   pip install -r requirements.txt

3. Run the app
   streamlit run app.py

4. Open your browser at
   http://localhost:8501

How It Works:

1. The dataset contains past loan applications with details like income, credit history, employment status, and loan amount.
2. Missing values were filled and text columns like Gender and Education were converted into numbers.
3. New features were engineered — DTI ratio, EMI, and income-loan ratio — to better capture real-world lending logic.
4. A Gradient Boosting Classifier was trained on 80% of the data and tested on the remaining 20%, achieving 80% accuracy.
5. The trained model is saved and loaded into a Streamlit web app where users enter their details and get an instant prediction.


## Project Structure

loan-eligibility-predictor

app.py              # Streamlit web app

model.pkl           # Trained ML model

columns.pkl         # Feature column order

train.csv           # Dataset

requirements.txt    # Dependencies

README.md           # Project documentation


## Author

Srisha Jha — First year CS student
GitHub: github.com/srishajha

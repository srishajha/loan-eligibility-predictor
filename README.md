Link to the live app- https://srishajha-loan-eligibility-predictor.streamlit.app/
This app predicts whether a bank should approve or reject a loan application based on the applicant's income, credit history, and other details.
I built this as my first ML project to explore model training, and deployment.
Trained a Random Forest classifier on Kaggle's loan prediction dataset. Cleaned missing values, encoded categorical features, and achieved 80% accuracy.
## Run Locally:
1. Clone the repository
   git clone https://github.com/srishajha/loan-eligibility-predictor.git
2. Navigate into the folder
   cd loan-eligibility-predictor
3. Install dependencies
   pip install -r requirements.txt
4. Run the app
   streamlit run app.py
5. Open your browser at
   http://localhost:8501

# CustomerChurnApp
A Machine Learning based Customer Churn Prediction Web App built using Streamlit. Predicts whether a customer will stay or leave based on age, gender, tenure, services, and charges
# 📊 Customer Churn Prediction – Streamlit Web App

A Machine Learning–powered **Customer Churn Prediction Web App** built using  
**Python, Streamlit, Scikit-learn, Pandas, and Random Forest Classifier**.

This app predicts whether a telecom customer is likely to **Churn (Leave)** or **Stay**,  
based on features like age, gender, tenure, services, and billing information.

---

## 🚀 Live Demo
(You will put your Streamlit Cloud URL here after deployment)

---

## 📁 Project Structure

CustomerChurnProject/
│
├── app.py # Streamlit Web App
├── churn.py # ML model training script
├── churn_model.pkl # Trained Random Forest model
├── requirements.txt # Dependencies
│
├── dataset/
│ └── customer_churn.csv # Dataset used for training
│
└── venv/ (optional) # Virtual environment (not uploaded to GitHub)

yaml
Copy code

---

## 🧠 Machine Learning Pipeline

### ✔ 1. Data Cleaning  
- Missing values handled  
- Categorical values encoded using LabelEncoder  
- Age column used instead of SeniorCitizen  

### ✔ 2. Feature Engineering  
- Customer demographic details  
- Subscription information  
- Charges  
- Tenure  

### ✔ 3. Model Training  
Model used: **Random Forest Classifier**

Trained using:

```py
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)
✔ 4. Model Evaluation
Accuracy score

Classification Report

Saved as churn_model.pkl

🎨 Streamlit Web App Features
Clean and simple UI

User inputs:

Customer ID

Gender

Age (15–55)

Partner / Dependents

Phone Service

Tenure

Monthly Charges

Total Charges

Predict Button → Shows
✔ Customer will stay
❌ Customer is likely to churn

▶️ How to Run Locally
1️⃣ Clone the Repo
bash
Copy code
git clone https://github.com/YOUR_USERNAME/CustomerChurnApp.git
cd CustomerChurnApp
2️⃣ Install Requirements
bash
Copy code
pip install -r requirements.txt
3️⃣ Run Streamlit App
bash
Copy code
streamlit run app.py
☁️ Deploy on Streamlit Cloud
Go to: https://share.streamlit.io

Connect your GitHub

Select your repository

Branch: main

Main file path: app.py

Deploy

📷 Screenshots (optional)
You can add screenshots after app deployment.

🛠 Technologies Used
Python

Streamlit

Pandas

Scikit-learn

Random Forest

GitHub

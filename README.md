# Customer Churn App
# 📊 Customer Churn Prediction – Streamlit Web App

A complete **Machine Learning + Streamlit** project that predicts whether a telecom customer will **Churn (Leave)** or **Stay** based on demographic and service usage data.

## 🚀 Live Demo  
(https://customerchurnapp-h6hpgkxan5g8enyqy6vbej.streamlit.app/)

---

# 🖼 Screenshots

### 🏠 Home Screen  

![<img width="2857" height="1618" alt="Screenshot 2025-11-22 042611" src="https://github.com/user-attachments/assets/53a38808-d2d2-4b03-a4f6-afa6ca2612a8" />
](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/screenshots/home.png)

### 🧮 Prediction Example  

![<img width="2837" height="1628" alt="Screenshot 2025-11-22 042631" src="https://github.com/user-attachments/assets/f01b7bcf-52b2-495e-9484-306e777f2052" />
](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/screenshots/predict.png)


---

# 📁 Project Structure
CustomerChurnApp/

│

├── app.py # Streamlit Web App (Final)

├── churn.py # ML Training Script

├── churn_model.pkl # Trained Random Forest Model

├── requirements.txt # Python Dependencies

├── README.md # Project Documentation

├── .gitignore

│
└── dataset/

└── customer_churn.csv # Dataset used for training


---

# 🧠 Machine Learning Overview

### 🔹 1. Data Processing
- Cleaned dataset  
- Encoded categorical fields  
- Added `Age (15–55)` instead of `SeniorCitizen`  
- Removed duplicates & missing values  

### 🔹 2. Model Training
Model used:

```python
RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)
🔹 3. Outputs

Accuracy score

Classification report

Final ML model: churn_model.pkl

🎨 Streamlit App Features

Users can input:

Customer ID

Gender

Age (15–55)

Partner

Dependents

Phone Service

Tenure

Monthly Charges

Total Charges

➡️ App predicts:

✔ Customer Will Stay

❌ Customer Will Churn

||...||

▶️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
streamlit run app.py

☁️ Deploying to Streamlit Cloud

Go to https://share.streamlit.io

Connect your GitHub

Select repository: CustomerChurnApp

Branch: main

Main file: app.py

Deploy! 🚀

🛠 Tech Stack

Python

Streamlit

Pandas

NumPy

Scikit-Learn

Random Forest

👨‍💻 Author

Nitish — AI/ML Developer

GitHub: https://github.com/nk264-art

Project Repo: (Add your repo link here)

⭐ Support

If you like this project, please ⭐ star the repository!

# 🚦 TrafficTelligence: Traffic Volume Prediction with Machine Learning

TrafficTelligence is a machine learning web app that predicts hourly traffic volume based on environmental and temporal factors. It uses XGBoost Regression for accurate predictions and a Flask web interface for user-friendly access.

---

## 📁 Project Structure

TrafficTelligence-ML/
│
├── app/
│ ├── app.py # Flask backend
│ └── templates/
│ └── index.html # Web form UI
│
├── data/
│ └── traffic_volume.csv # Raw dataset
│
├── output/
│ ├── xgb_model.pkl # Trained model
│ └── scaler.pkl # Feature scaler
│
├── notebooks/
│ └── traffic_analysis.ipynb # EDA and training code
│
├── requirements.txt # Dependencies
└── README.md # Project overview


---

## 📊 Features Used

- Temperature (K)
- Rain (mm)
- Snow (mm)
- Hour of Day (0–23)
- Day of Week (0=Monday, ..., 6=Sunday)
- Month (1–12)

---

## 🚀 How to Run

### 1. Clone or Download the Repository
```bash
git clone https://github.com/yourusername/TrafficTelligence.git
cd TrafficTelligence-ML

2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt
3. Run the Web App
bash
Copy
Edit
cd app
python app.py
Then open your browser at:
http://127.0.0.1:5000

✅ Sample Prediction
Input Feature	Value
Temperature	289.0
Rain	0.0
Snow	0.0
Hour	8
Day of Week	1 (Tuesday)
Month	6 (June)

→ Predicted Traffic Volume: 5161 (example)

📈 Model Performance
Model Used: XGBoost Regressor

R² Score: 0.94

RMSE: ~467

🛠 Built With
Python

Scikit-learn

XGBoost

Flask

HTML/CSS (Jinja2 templating)

📌 Acknowledgment
Dataset Source: SmartInternz Traffic Volume Dataset

Internship: SmartInternz AI-ML Internship

👨‍💻 Developed By
Akash
B.Tech CSE, JNTUACEP
SmartInternz Machine Learning Internship (2025)


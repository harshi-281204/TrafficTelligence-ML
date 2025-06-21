# TrafficTelligence: Advanced Traffic Volume Estimation with Machine Learning

TrafficTelligence is a machine learning-based web application that predicts traffic volume using historical weather and time data. Built with XGBoost for regression, Flask for deployment, and pandas for preprocessing, this project aims to assist in smarter urban traffic management.

---

## 📈 Problem Statement

Estimate traffic volume based on weather and time-related features to help urban planners and commuters with more informed decisions.

---

## 🤖 Tech Stack

* **Frontend**: HTML (Jinja2 via Flask)
* **Backend**: Python (Flask)
* **Model**: XGBoost Regressor
* **Libraries**: pandas, scikit-learn, matplotlib, seaborn, joblib
* **Deployment**: Flask local server

---

## 📊 Features Used

* Temperature
* Rainfall
* Snowfall
* Hour
* Day of Week
* Month

---

## 📁 Folder Structure

```
TrafficTelligence-ML/
├── app/
│   ├── app.py               # Flask backend
│   └── templates/
│       └── index.html       # Web form UI
├── data/
│   └── traffic_volume.csv   # Raw dataset
├── notebooks/
│   ├── traffic_analysis.ipynb      # Original EDA & model
│   └── traffic_analysis_v2.ipynb   # Updated version
├── output/
│   ├── xgb_model.pkl        # Trained model
│   └── scaler.pkl           # StandardScaler object
├── readme/
│   └── readme.md            # Project explanation (optional folder)
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

---

## 🚀 Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/akashmandala/TrafficTelligence-ML.git
cd TrafficTelligence-ML
```

### 2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the app:

```bash
cd app
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🔹 Sample Usage

Input:

* Temperature: `295`
* Rain: `0.2`
* Snow: `0.0`
* Hour: `17`
* Day of Week: `4`
* Month: `8`

Output:

```
Predicted Traffic Volume: 4873
```

---

## 🔧 Model Performance

* **Algorithm**: XGBoost Regressor
* **RMSE**: \~466
* **R^2 Score**: 0.94 (on final model)

---

## 📄 Author

**Akash Mandala**
B.Tech CSE, JNTUACEP (2022–2026)
Machine Learning & Full Stack Developer

---

## 📦 License

This project is open-source and available under the MIT License.

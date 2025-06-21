from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("../output/xgb_model.pkl")
scaler = joblib.load("../output/scaler.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input from form
        temp = float(request.form['temp'])
        rain = float(request.form['rain'])
        snow = float(request.form['snow'])
        hour = int(request.form['hour'])
        dayofweek = int(request.form['dayofweek'])
        month = int(request.form['month'])

        features = np.array([[temp, rain, snow, hour, dayofweek, month]])
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        return render_template('index.html', prediction=int(prediction))

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

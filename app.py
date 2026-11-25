
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained Random Forest model
model = joblib.load('models/crop.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get values from website form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Keep the same feature names and order used during training
        input_data = pd.DataFrame([[
            N, P, K, temperature, humidity, ph, rainfall
        ]], columns=[
            'N', 'P', 'K', 'temperature',
            'humidity', 'ph', 'rainfall'
        ])

        # Predict crop
        prediction = model.predict(input_data)[0]

        return render_template(
            'index.html',
            prediction=prediction
        )

    except Exception as e:
        return render_template(
            'index.html',
            error="Please enter valid input values."
        )


if __name__ == '__main__':
    app.run(debug=True)

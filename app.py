from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the AI model
model = pickle.load(open('ai_model/cibil_model.pkl', 'rb'))

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Predict Page
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        income = int(request.form['income'])
        loan_amount = int(request.form['loan_amount'])
        existing_loans = int(request.form['existing_loans'])

        features = np.array([[age, income, loan_amount, existing_loans]])
        score = model.predict(features)[0]

        banks = []
        if score >= 750:
            banks = [
                {"name": "HDFC Bank", "amount": "₹20 Lakhs"},
                {"name": "ICICI Bank", "amount": "₹18 Lakhs"},
                {"name": "Axis Bank", "amount": "₹15 Lakhs"}
            ]
        elif 650 <= score < 750:
            banks = [
                {"name": "SBI Bank", "amount": "₹10 Lakhs"},
                {"name": "PNB Bank", "amount": "₹8 Lakhs"}
            ]
        else:
            banks = [
                {"name": "Local Cooperative Bank", "amount": "₹2 Lakhs"}
            ]

        return render_template('result.html', score=score, banks=banks)

if __name__ == '__main__':
    app.run(debug=True)
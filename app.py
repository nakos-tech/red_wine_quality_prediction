from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
import pandas as pd
from src.my_project.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/train", methods=['POST'])
# def train():
#     os.system("python main.py")
#     return"training completed successfully"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None

    if request.method == "POST":
        try:
            # Get form data from the request
            input_data = {
                'fixed_acidity': float(request.form['fixed_acidity']),
                'volatile_acidity': float(request.form['volatile_acidity']),
                'citric_acid': float(request.form['citric_acid']),
                'residual_sugar': float(request.form['residual_sugar']),
                'chlorides': float(request.form['chlorides']),
                'free_sulfur_dioxide': float(request.form['free_sulfur_dioxide']),
                'total_sulfur_dioxide': float(request.form['total_sulfur_dioxide']),
                'density': float(request.form['density']),
                'pH': float(request.form['pH']),
                'sulphates': float(request.form['sulphates']),
                'alcohol': float(request.form['alcohol'])
            }

            # Convert to NumPy array and reshape
            data = np.array(list(input_data.values())).reshape(1, -1)

            # Prediction pipeline
            obj = PredictionPipeline()
            prediction = obj.predict(data)[0]

        except Exception as e:
            prediction = f"Error: {e}"

    # Render form template with prediction result
    return render_template("index.html", prediction=prediction)

 



if __name__ == '__main__':
    app.run(debug=True)

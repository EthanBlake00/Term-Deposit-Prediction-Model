import requests
from flask import Flask, render_template
import joblib as jb

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the model
        logistic_model = jb.load("build_models/logistic_model.pkl")

    except Exception as e:
        print("Error loading model: " + str(e))
        return "Error loading model: " + str(e)
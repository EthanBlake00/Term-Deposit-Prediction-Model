from flask import Flask, render_template, request

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utils.main import make_prediction

app = Flask(__name__)

# Initialize Limiter correctly
limiter = Limiter(get_remote_address, app=app)

@app.route('/')
@limiter.limit("10 per minute")
def home():
    return render_template('index.html')

@app.route('/about')
@limiter.limit("10 per minute")
def about():
    return render_template('about.html')
@app.route('/predict', methods=['POST'])
@limiter.limit("5 per minute")
def predict():
    try:
        # Extract and validate inputs
        age = request.form.get('age')
        campaign = request.form.get('campaign')
        pdays = request.form.get('pdays')
        previous = request.form.get('previous')

        if not all([age, campaign, pdays, previous]):
            return "Error: Missing data"

        age = int(age)
        campaign = int(campaign)
        pdays = int(pdays)
        previous = int(previous)

        job = request.form.get('job')
        marital = request.form.get('marital')
        education = request.form.get('education')
        default = request.form.get('default')
        loan = request.form.get('loan')
        housing = request.form.get('housing')
        poutcome = request.form.get('poutcome')

        if not all([job, marital, education, default, loan, housing, poutcome]):
            return "Error: Missing data"

        # Prepare input array
        x = [[age, job, marital, education, default, loan, housing, campaign, pdays, previous, poutcome]]
        print(f"Input Features: {x}")

        prediction_result =  make_prediction(x)
        print(f"Prediction Result: {prediction_result}")
        return  render_template('result.html', prediction=prediction_result)

    except ValueError as ve:
        return f"Error: Invalid data format - {str(ve)}"
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
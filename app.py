from flask import Flask, render_template, request

from utils.main import make_prediction

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
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

        return make_prediction(x)

    except ValueError as ve:
        return f"Error: Invalid data format - {str(ve)}"
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
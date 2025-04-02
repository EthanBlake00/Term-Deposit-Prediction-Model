from flask import Flask, render_template, request

from utils.main import makePrediction

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the form
        age = int(request.form.get('age'))
        job = request.form.get('job')
        marital = request.form.get('marital')
        education = request.form.get('education')
        default = request.form.get('default')
        loan = request.form.get('loan')
        housing = request.form.get('housing')
        campaign = int(request.form.get('campaign'))
        pdays = int(request.form.get('pdays'))
        previous = int(request.form.get('previous'))
        poutcome = request.form.get('poutcome')

        # Ensure the inputs are valid
        if not all([age, job, marital, education, default, loan, housing, poutcome]):
            return "Error: Missing data"

        # Prepare the feature array for prediction
        x = [[age, job, marital, education, default, loan, housing, campaign, pdays, previous, poutcome]]
        print(f"Input Features: {x}")
        return makePrediction(x)

    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)

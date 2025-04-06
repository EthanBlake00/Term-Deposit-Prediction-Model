# Term Deposit Prediction Model
This repository contains a machine learning model for predicting term deposit subscriptions using the UCI Bank Marketing dataset. The model is built using Python and various libraries such as Pandas, NumPy, Scikit-learn, and Matplotlib.
The model is trained to predict whether a client will subscribe to a term deposit based on various features such as age, job, marital status, education, and more.

## Dataset
The dataset used for this project is the UCI Bank Marketing dataset, which contains information about clients of a Portuguese banking institution. The dataset includes various features such as:
- Age
- Job
- Marital status
- Education
- Default status
- Balance
- Housing loan status
- Personal loan status
- Contact communication type
- Last contact month of the year
- Last contact day of the month
- Last contact duration
- Number of contacts performed during this campaign
- Number of contacts performed before this campaign
- Outcome of the previous marketing campaign
- Number of days since the client was last contacted from a previous campaign
- Number of contacts performed during this campaign
- Outcome of the previous marketing campaign
-  .......ect
- Target variable: whether the client subscribed to a term deposit (yes/no)

You can download the dataset from the UCI Machine Learning Repository: [Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/bank+marketing).

## Installation
To run this project, you need to have Python 3.x installed on your machine. You can install the required libraries using pip:
```bash
  pip install -r requirements.txt
```
## Usage
To run the model, you can use the following command:
```bash 
  gunicorn  -w 4 -b 0.0.0.0:5000 app:app
```
This will start a Flask server on port 5000. You can then access the model's API at `http://localhost:5000`.
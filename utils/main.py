import joblib as jb
import numpy as np

def makePrediction(x: list) -> str:
    # Transform categorical features using the column transformer
    ct = jb.load('build_models/ct.pkl')
    x = np.array(ct.transform(x))
    print(f"Transformed Features: {x}")

    # Scale the features if needed
    sc = jb.load('build_models/scaler.pkl')
    x[:, -4:-1] = sc.transform(x[:, -4:-1])  # Ensure correct column slicing
    print(f"Scaled Features: {x}")

    # Load the model
    model = jb.load('build_models/logistic_model.pkl')
    prediction = model.predict(x)
    print(f"Prediction: {prediction}")

    # Return prediction result as a response
    if prediction == 0:
        return "The client will not subscribe to a term deposit."
    else:
        return "The client will subscribe to a term deposit."
import joblib as jb
import numpy as np

def make_prediction(x: list) -> str:
    try:
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
            return "No"
        else:
            return "Yes"

    except FileNotFoundError as e:
        print(f"Error: One or more model files were not found - {str(e)}")
        return "Error: Model files not found."
    except ValueError as e:
        print(f"Error: Data type mismatch or invalid value - {str(e)}")
        return "Error: Invalid input data."
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return f"Error: {str(e)}"

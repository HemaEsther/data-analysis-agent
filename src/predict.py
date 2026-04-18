import pandas as pd
import joblib


def predict_new_data(file_path, save_output=False):
    try:
        # -------------------------
        # Load model
        # -------------------------
        model = joblib.load("best_model.pkl")
        print(" Model loaded")

        # -------------------------
        # Load data
        # -------------------------
        df = pd.read_csv(file_path)
        print(f" Data loaded ({df.shape[0]} rows)")

        # -------------------------
        # Predict
        # -------------------------
        preds = model.predict(df)
        df["Prediction"] = preds

        print(" Predictions generated")

        # -------------------------
        # Optional save
        # -------------------------
        if save_output:
            df.to_csv("predictions.csv", index=False)
            print(" Saved as 'predictions.csv'")

        return df

    except FileNotFoundError:
        print(" Model file not found. Train model first.")
    except Exception as e:
        print(f" Prediction failed: {e}")
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix, classification_report



#  Target Detection

def detect_target_column(df):
    priority = ['target', 'label', 'y', 'output']

    for col in priority:
        if col in df.columns:
            return col

    for col in df.columns:
        if "date" in col.lower():
            continue

        if df[col].nunique() == 2:
            return col

    return df.columns[-1]



#  Problem Type Detection

def detect_problem_type(y):
    if y.dtype == "object" or y.dtype.name == "category":
        return "classification"

    unique_vals = sorted(y.dropna().unique())

    if len(unique_vals) == 2:
        return "classification"

    return "regression"



#  Training Pipeline

def train_models(df, target_col=None):

    print("\n Training Models...\n")

    
    # Clean dataset
    
    df = df.dropna(axis=1, how='all')

    df = df.loc[:, df.nunique() > 1]

    if df.empty:
        print(" Dataset empty")
        return None

    
    #  FIX: DO NOT override user target
    
    if target_col is None:
        target_col = detect_target_column(df)

    elif target_col not in df.columns:
        raise ValueError(f" Target column '{target_col}' not found in dataset")

    print(f"Target: {target_col}")

    # -------------------------
    # Remove missing target rows
    # -------------------------
    df = df[df[target_col].notnull()]
    if df.empty:
        print(" No target data")
        return None

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # -------------------------
    #  REMOVE DATE COLUMNS (leakage)
    # -------------------------
    X = X.drop(columns=[col for col in X.columns if "date" in col.lower()], errors="ignore")

    # -------------------------
    #  EXTRA LEAKAGE CHECK
    # -------------------------
    if target_col in X.columns:
        print(" Leakage detected: target present in features")
        X = X.drop(columns=[target_col])

    # -------------------------
    # Encode target if categorical
    # -------------------------
    if y.dtype == "object":
        y = y.astype("category").cat.codes

    print(f"Unique target values: {y.unique()[:5]}")

    # -------------------------
    # Detect problem type
    # -------------------------
    problem = detect_problem_type(y)
    print(f"Problem Type: {problem.upper()}")

    # -------------------------
    # Train-test split
    # -------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------
    # Feature pipelines
    # -------------------------
    num_cols = X.select_dtypes(include=['number']).columns
    cat_cols = X.select_dtypes(include=['object']).columns

    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, cat_cols)
    ])

    # -------------------------
    # Models
    # -------------------------
    if problem == "classification":
        models = {
            "Logistic Regression": LogisticRegression(max_iter=1000),
            "Random Forest": RandomForestClassifier()
        }
    else:
        models = {
            "Linear Regression": LinearRegression(),
            "Random Forest Regressor": RandomForestRegressor()
        }

    results = {}
    trained_models = {}

    # -------------------------
    # Training loop
    # -------------------------
    for name, model in models.items():
        print(f"\nTraining {name}...")

        pipeline = Pipeline([
            ("preprocessing", preprocessor),
            ("model", model)
        ])

        try:
            pipeline.fit(X_train, y_train)
            preds = pipeline.predict(X_test)

            trained_models[name] = pipeline

            if problem == "classification":
                score = accuracy_score(y_test, preds)
                results[name] = score

                print(f"Accuracy: {score:.2f}")

                # -------------------------
                #  Confusion Matrix
                # -------------------------
                cm = confusion_matrix(y_test, preds)

                print("Confusion Matrix:")
                print(f"TN: {cm[0][0]}  FP: {cm[0][1]}")
                print(f"FN: {cm[1][0]}  TP: {cm[1][1]}")

                print("\nClassification Report:")
                print(classification_report(y_test, preds))

            else:
                rmse = np.sqrt(mean_squared_error(y_test, preds))
                r2 = r2_score(y_test, preds)

                results[name] = r2
                print(f"RMSE: {rmse:.2f}")
                print(f"R2: {r2:.2f}")

        except Exception as e:
            print(f"{name} failed: {e}")

    # -------------------------
    # Handle failure
    # -------------------------
    if not results:
        print(" All models failed")
        return None

    # -------------------------
    # Select best model
    # -------------------------
    best_model = max(results, key=results.get)
    best_score = results[best_model]

    print(f"\n Best Model: {best_model}")

    # -------------------------
    # Save model
    # -------------------------
    joblib.dump(trained_models[best_model], "best_model.pkl")

    return best_score
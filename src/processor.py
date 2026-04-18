import pandas as pd
import numpy as np


def process_data(df, target=None):
    df = df.copy()

    print("\n Processing dataset...\n")

    # -------------------------
    # 1. Handle Missing Values
    # -------------------------
    for col in df.columns:
        if col == target:
            continue

        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode().iloc[0] if not df[col].mode().empty else "Unknown")

    # -------------------------
    # 2. Drop constant columns
    # -------------------------
    constant_cols = [col for col in df.columns if col != target and df[col].nunique() == 1]
    df = df.drop(columns=constant_cols)

    # -------------------------
    # 3. Encode categorical
    # -------------------------
    cat_cols = df.select_dtypes(include=['object']).columns

    for col in cat_cols:
        if col == target:
            continue

        if df[col].nunique() < 10:
            df[col] = df[col].astype('category').cat.codes
        else:
            df = pd.get_dummies(df, columns=[col], drop_first=True)

    # -------------------------
    # 4. Handle skewness
    # -------------------------
    num_cols = df.select_dtypes(include=['number']).columns

    for col in num_cols:
        if col == target:
            continue

        if df[col].min() >= 0 and abs(df[col].skew()) > 1:
            df[col] = np.log1p(df[col])

    # -------------------------
    # 5. Handle outliers (IQR)
    # -------------------------
    for col in num_cols:
        if col == target:
            continue

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df[col] = np.clip(df[col], lower, upper)

    print(" Data cleaned successfully\n")

    return df
import pandas as pd


# -------------------------
#  Basic Info
# -------------------------
def get_basic_info(df):
    return df.shape


def preview_data(df, show_preview=True):
    if show_preview:
        print("\n Dataset Preview")
        print(df.head())

    print(f"\nShape: {df.shape}\n")
# -------------------------
#  Missing Values
# -------------------------
def get_missing_info(df):
    return (df.isnull().mean() * 100).to_dict()


# -------------------------
#  Dataset Optimization
# -------------------------
def auto_optimize_dataset(df, sample_size=10000):
    rows = df.shape[0]

    if rows > 100000:
        print(f"\n Large dataset ({rows} rows) → sampling {sample_size}")
        df = df.sample(sample_size, random_state=42)
    else:
        print("\n Dataset size OK")

    return df


# -------------------------
#  Feature Types
# -------------------------
def get_feature_types(df):
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    return num_cols, cat_cols


# -------------------------
#  Skewness
# -------------------------
def get_skewness(df, num_cols):
    return df[num_cols].skew().to_dict()


# -------------------------
#  Correlation
# -------------------------
def get_correlation(df, num_cols):
    return df[num_cols].corr()
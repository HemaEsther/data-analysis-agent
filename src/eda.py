def get_basic_info(df):
    return df.shape

def get_missing_info(df):
    missing = {}
    for col in df.columns:
        miss_pct = (df[col].isnull().sum() / len(df)) * 100
        missing[col] = miss_pct
    return missing

def preview_data(df):
    print("\n🔍 Dataset Preview:")
    print(df.head())

    print("\n📏 Shape:", df.shape)

    print("\n🧾 Info:")
    print(df.info())


def check_dataset_size(df):
    rows, cols = df.shape

    print("\n📊 Dataset Size Check:")

    if rows > 100000:
        print(f"⚠️ Large dataset detected ({rows} rows)")
        return True
    else:
        print(f"✅ Dataset size is manageable ({rows} rows)")
        return False


def smart_sampling(df):
    print("\n💡 Suggestion: Large dataset may slow analysis")

    choice = input("👉 Sample 10,000 rows? (y/n): ").lower()

    if choice == "y":
        df = df.sample(10000, random_state=42)
        print("✅ Sampled dataset shape:", df.shape)

    return df

def get_feature_types(df):
    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(include=['object']).columns
    return num_cols, cat_cols

def get_skewness(df, num_cols):
    skewness = {}
    for col in num_cols:
        skewness[col] = df[col].skew()
    return skewness

def get_correlation(df, num_cols):
    return df[num_cols].corr()
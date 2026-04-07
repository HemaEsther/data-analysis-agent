def interpret_missing(missing_dict):
    for col, pct in missing_dict.items():
        if pct > 30:
            print(f"⚠️ {col} has high missing values ({pct:.2f}%)")
        elif pct > 0:
            print(f"ℹ️ {col} has some missing values ({pct:.2f}%)")

def interpret_skewness(skew_dict):
    for col, skew in skew_dict.items():
        if skew > 1:
            print(f"⚠️ {col} is highly right-skewed")
        elif skew < -1:
            print(f"⚠️ {col} is highly left-skewed")
        else:
            print(f"✅ {col} is fairly normal")

def interpret_correlation(corr):
    for col in corr.columns:
        for row in corr.index:
            if col != row and abs(corr.loc[row, col]) > 0.8:
                print(f"🔥 Strong correlation between {row} and {col}")

# Add “RECOMMENDATION ENGINE

def feature_recommendations(df):
    print("\n📌 FEATURE SELECTION RECOMMENDATIONS\n")
    
    # High missing values
    for col in df.columns:
        miss_pct = (df[col].isnull().sum() / len(df)) * 100
        
        if miss_pct > 50:
            print(f"❌ Consider DROPPING '{col}' (very high missing values: {miss_pct:.2f}%)")
    
    # Correlation-based removal
    num_cols = df.select_dtypes(include=['number']).columns
    corr = df[num_cols].corr()
    
    removed = set()
    
    for col in corr.columns:
        for row in corr.index:
            if col != row and abs(corr.loc[row, col]) > 0.9:
                if row not in removed:
                    print(f"⚠️ '{row}' and '{col}' are highly correlated → consider removing one")
                    removed.add(row)

# Model Suggestion Logic
def model_recommendation(df):
    print("\n🤖 MODEL RECOMMENDATION\n")
    
    # Check if target exists
    if 'target' in df.columns:
        unique_vals = df['target'].nunique()
        
        if unique_vals <= 10:
            print("👉 Classification Problem detected")
            print("Recommended Models: Logistic Regression, Random Forest, XGBoost")
        else:
            print("👉 Regression Problem detected")
            print("Recommended Models: Linear Regression, Random Forest Regressor")
    else:
        print("👉 No target column found → EDA only dataset")
        print("👉 If predicting pollution → use Regression models")

# Imbalance Detection

def check_imbalance(df):
    print("\n⚖️ DATA IMBALANCE CHECK\n")
    
    if 'target' in df.columns:
        counts = df['target'].value_counts(normalize=True)
        
        if counts.max() > 0.7:
            print("⚠️ Dataset is IMBALANCED")
            print("👉 Use: F1-score, Precision, Recall")
        else:
            print("✅ Dataset is balanced")
            print("👉 Use: Accuracy")
    else:
        print("👉 No classification target → imbalance not applicable")

# Preprocessing Suggestions
def preprocessing_suggestions(df):
    print("\n🛠️ PREPROCESSING SUGGESTIONS\n")
    
    num_cols = df.select_dtypes(include=['number']).columns
    
    for col in num_cols:
        skew = df[col].skew()
        
        if abs(skew) > 1:
            print(f"📊 Apply log transformation on '{col}' (skewed)")
    
    print("👉 Handle missing values using mean/median imputation")
    print("👉 Scale numerical features if using distance-based models")

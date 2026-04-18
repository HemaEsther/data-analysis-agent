from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# -------------------------
#  Global Risk Summary
# -------------------------
def global_risk_summary(issues):
    print("\n DATA HEALTH")

    if "missing" in issues:
        print("• Missing values present")

    if "skew" in issues:
        print("• Skewed features detected")

    if "correlation" in issues:
        print("• High feature correlation")


# -------------------------
#  Baseline Model (Optional)
# -------------------------
def train_before_processing(df, target):
    try:
        df = df.dropna()

        X = df.drop(columns=[target])
        y = df[target]

        model = LinearRegression()
        model.fit(X, y)

        preds = model.predict(X)
        return r2_score(y, preds)

    except:
        return None


# -------------------------
#  Trust Score
# -----------------------
def calculate_trust_score(df, target, score, corr):
    trust = 100
    reasons = []

    # Suspiciously high score
    if score and score > 0.98:
        trust -= 30
        reasons.append("Very high score → possible overfitting")

    # Correlation with target
    try:
        if corr[target].abs().max() > 0.9:
            trust -= 25
            reasons.append("High correlation with target")
    except:
        pass

    # Dataset size
    if df.shape[0] < 1000:
        trust -= 10
        reasons.append("Small dataset")

    # Level
    if trust >= 80:
        level = "HIGH"
    elif trust >= 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    return trust, level, reasons


# -------------------------
#  Smart Suggestions
# -------------------------
def smart_suggestions(score, issues):
    print("\n NEXT STEPS")

    if score and score > 0.95:
        print("• Validate using cross-validation")

    if "correlation" in issues:
        print("• Apply feature selection")

    if "skew" in issues:
        print("• Try transformation (log / Box-Cox)")

    print("• Try advanced models (XGBoost, LightGBM)")
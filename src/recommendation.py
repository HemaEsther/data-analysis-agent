import numpy as np


# -------------------------
#  Generate Recommendations
# -------------------------
def generate_recommendations(df):
    recs = []
    num_cols = df.select_dtypes(include=['number']).columns

    for col in num_cols:

        # Missing
        missing_pct = df[col].isnull().mean() * 100
        if missing_pct > 0:
            recs.append({
                "column": col,
                "issue": f"Missing values ({missing_pct:.1f}%)",
                "action": "Apply median imputation",
                "priority": 5 if missing_pct > 30 else 3
            })

        # Skew
        skew = df[col].skew()
        if abs(skew) > 1:
            recs.append({
                "column": col,
                "issue": f"High skew ({skew:.2f})",
                "action": "Apply log transformation",
                "priority": 4
            })

        # Outliers
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()

        if outliers > 0:
            recs.append({
                "column": col,
                "issue": f"{outliers} outliers detected",
                "action": "Apply IQR capping",
                "priority": 3
            })

    return recs


# -------------------------
#  Correlation Recommendations
# -------------------------
def add_correlation_recommendations(df, recs):
    corr = df.corr(numeric_only=True)
    seen = set()

    for col1 in corr.columns:
        for col2 in corr.columns:
            if col1 >= col2:
                continue

            if abs(corr.loc[col1, col2]) > 0.85:
                pair = (col1, col2)

                if pair not in seen:
                    recs.append({
                        "column": f"{col1} & {col2}",
                        "issue": "High correlation",
                        "action": f"Drop one of them",
                        "priority": 4
                    })
                    seen.add(pair)

    return recs


# -------------------------
#  Clean Print
# -------------------------
def print_recommendations(recs, limit=10):
    recs = sorted(recs, key=lambda x: x.get("priority", 0), reverse=True)[:limit]

    print("\n KEY RECOMMENDATIONS\n")

    for r in recs:
        print(f"• {r['column']} → {r['issue']}")
        print(f"  Action: {r['action']}")
def detect_data_issues(df, missing, skew, corr):
    print("\n DATA ISSUES\n")

    issues_found = False

    # Missing
    for col, pct in missing.items():
        if pct > 30:
            print(f"• {col}: high missing ({pct:.1f}%)")
            issues_found = True

    # Skew
    for col, val in skew.items():
        if abs(val) > 1:
            print(f"• {col}: skewed ({val:.2f})")
            issues_found = True

    # Correlation
    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i, j]) > 0.85:
                print(f"• {corr.columns[i]} ↔ {corr.columns[j]} (high correlation)")
                issues_found = True

    if not issues_found:
        print("• No major issues detected")



# OPTIONAL (clean summaries)


def interpret_missing(missing_dict):
    print("\n Missing Overview")
    for col, pct in missing_dict.items():
        if pct > 30:
            print(f"• {col}: high ({pct:.1f}%)")
        elif pct > 0:
            print(f"• {col}: low ({pct:.1f}%)")


def interpret_skewness(skew_dict):
    print("\n Skewness Overview")
    for col, val in skew_dict.items():
        if val > 1:
            print(f"• {col}: right skew")
        elif val < -1:
            print(f"• {col}: left skew")


def interpret_correlation(corr):
    print("\n Key Correlations")
    seen = set()

    for col in corr.columns:
        for row in corr.index:
            if col != row and abs(corr.loc[row, col]) > 0.85:
                pair = tuple(sorted([col, row]))
                if pair not in seen:
                    print(f"• {row} ↔ {col}")
                    seen.add(pair)
from src.eda import *
from src.insights import *
from src.processor import process_data
from src.model_trainer import *
from src.utils import global_risk_summary, train_before_processing, calculate_trust_score, smart_suggestions
from src.recommendation import generate_recommendations, add_correlation_recommendations, print_recommendations


class DataAnalysisAgent:

    def __init__(self, df, target_col=None):
        self.df = df
        self.target_col = target_col

    def run(self):
        print("STARTING ANALYSIS...\n")

        # -------------------------
        #  Preview + Optimization
        # -------------------------
        preview_data(self.df)
        self.df = auto_optimize_dataset(self.df)

        # -------------------------
        # Basic Info
        # -------------------------
        rows, cols = get_basic_info(self.df)
        print(f"\nDataset has {rows} rows and {cols} columns")

        # -------------------------
        #  Missing
        # -------------------------
        print("\n--- Missing Analysis ---")
        missing = get_missing_info(self.df)
        interpret_missing(missing)

        # -------------------------
        #  Feature Types
        # -------------------------
        print("\n--- Feature Types ---")
        num_cols, cat_cols = get_feature_types(self.df)
        print(f"Numerical: {len(num_cols)}, Categorical: {len(cat_cols)}")

        # -------------------------
        #  Skewness
        # -------------------------
        print("\n--- Skewness ---")
        skew = get_skewness(self.df, num_cols)
        interpret_skewness(skew)

        # -------------------------
        #  Correlation
        # -------------------------
        print("\n--- Correlation ---")
        corr = get_correlation(self.df, num_cols)
        interpret_correlation(corr)

        # -------------------------
        #  Data Issues
        # -------------------------
        detect_data_issues(self.df, missing, skew, corr)

        issues_detected = set()

        if any(v > 0 for v in missing.values()):
            issues_detected.add("missing")

        if any(abs(v) > 1 for v in skew.values()):
            issues_detected.add("skew")

        try:
            if corr.abs().max().max() > 0.85:
                issues_detected.add("correlation")
        except:
            pass

        global_risk_summary(issues_detected)

        # -------------------------
        #  Recommendations
        # -------------------------
        recs = generate_recommendations(self.df)
        recs = add_correlation_recommendations(self.df, recs)

        recs = sorted(recs, key=lambda x: x.get("priority", 0), reverse=True)
        recs = recs[:10]

        print_recommendations(recs)

        # -------------------------
        #  MODELING PIPELINE
        # -------------------------
        original_df = self.df.copy()

        try:
            before_score = train_before_processing(original_df, self.target_col)
        except:
            before_score = None

        # -------------------------
        #  FIX: Separate target BEFORE processing
        # -------------------------
        if self.target_col is None:
            raise ValueError(" Target column must be specified")

        if self.target_col not in self.df.columns:
            raise ValueError(f" Target '{self.target_col}' not found")

        target_series = self.df[self.target_col]
        feature_df = self.df.drop(columns=[self.target_col])

        # Process only features
        processed_features = process_data(feature_df, target=None)

        # Add target back
        processed_df = processed_features.copy()
        processed_df[self.target_col] = target_series

        # -------------------------
        #  Train Models
        # -------------------------
        best_score = train_models(processed_df, self.target_col)

        # -------------------------
        #  Trust Score
        # -------------------------
        score, level, reasons = calculate_trust_score(
            processed_df,
            self.target_col,
            best_score,
            processed_df.corr(numeric_only=True)
        )

        print("\n--- MODEL TRUST ---")
        print(f"• Score: {score}/100 ({level})")

        if reasons:
            print("• Concerns:")
            for r in reasons:
                print(f"  - {r}")

        # -------------------------
        #  Suggestions
        # -------------------------
        smart_suggestions(best_score, issues_detected)

        # -------------------------
        #  Final Summary
        # -------------------------
        print("\n==============================")
        print(" FINAL SUMMARY ")
        print("==============================")

        print(f"Dataset Size: {rows}")
        print(f"Target: {self.target_col}")

        if best_score:
            print(f"Model Score: {best_score:.2f}")

        print(f"Trust Level: {level}")
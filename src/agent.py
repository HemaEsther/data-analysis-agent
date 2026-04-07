# from src.eda import *
# from src.insights import *

# class DataAnalysisAgent:
    
#     def __init__(self, df):
#         self.df = df
    
#     def run(self):
#         print("🚀 Starting Agent...\n")
        
#         # Basic info
#         rows, cols = get_basic_info(self.df)
#         print(f"Dataset has {rows} rows and {cols} columns")
        
#         # Missing
#         print("\n--- Missing Analysis ---")
#         missing = get_missing_info(self.df)
#         interpret_missing(missing)
        
#         # Feature types
#         print("\n--- Feature Types ---")
#         num_cols, cat_cols = get_feature_types(self.df)
#         print(f"Numerical: {len(num_cols)}, Categorical: {len(cat_cols)}")
        
#         # Skewness
#         print("\n--- Skewness ---")
#         skew = get_skewness(self.df, num_cols)
#         interpret_skewness(skew)
        
#         # Correlation
#         print("\n--- Correlation ---")
#         corr = get_correlation(self.df, num_cols)
#         interpret_correlation(corr)
        
#         # 🔥 NEW SECTION (MOST IMPORTANT)
#         print("\n==============================")
#         print("🧠 INTELLIGENT RECOMMENDATIONS")
#         print("==============================")
        
#         feature_recommendations(self.df)
#         model_recommendation(self.df)
#         check_imbalance(self.df)
#         preprocessing_suggestions(self.df)
        
#         print("\n✅ Analysis Complete")


from src.eda import *
from src.insights import *
import io
import sys
from src.report import generate_report

class DataAnalysisAgent:
    
    def __init__(self, df):
        self.df = df
    
    def run(self):
        print("🚀 Starting Agent...\n")

        # ✅ NEW: Preview
        preview_data(self.df)

        # ✅ NEW: Size check
        is_large = check_dataset_size(self.df)

        # ✅ NEW: Smart sampling
        if is_large:
            self.df = smart_sampling(self.df)

        # -------------------------
        # Existing pipeline
        # -------------------------

        # Basic info
        rows, cols = get_basic_info(self.df)
        print(f"\nDataset has {rows} rows and {cols} columns")
        
        # Missing
        print("\n--- Missing Analysis ---")
        missing = get_missing_info(self.df)
        interpret_missing(missing)
        
        # Feature types
        print("\n--- Feature Types ---")
        num_cols, cat_cols = get_feature_types(self.df)
        print(f"Numerical: {len(num_cols)}, Categorical: {len(cat_cols)}")
        
        # Skewness
        print("\n--- Skewness ---")
        skew = get_skewness(self.df, num_cols)
        interpret_skewness(skew)
        
        # Correlation
        print("\n--- Correlation ---")
        corr = get_correlation(self.df, num_cols)
        interpret_correlation(corr)
        
        # 🔥 INTELLIGENT RECOMMENDATIONS
        print("\n==============================")
        print("🧠 INTELLIGENT RECOMMENDATIONS")
        print("==============================")
        
        # ✅ Capture printed insights
        buffer = io.StringIO()
        sys.stdout = buffer

        feature_recommendations(self.df)
        model_recommendation(self.df)
        check_imbalance(self.df)
        preprocessing_suggestions(self.df)

        sys.stdout = sys.__stdout__

        insights_text = buffer.getvalue()

# ALSO print it normally
        print(insights_text)

# ✅ REPORT GENERATION
        summary = self.df.describe()
        missing = self.df.isnull().sum()

        generate_report(self.df, summary, missing, insights_text)
        
print("\n✅ Analysis Complete")
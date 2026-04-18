import os
from src.data_loader import load_data
from src.agent import DataAnalysisAgent


# -------------------------
#  Get datasets
# -------------------------
def list_datasets(folder="data"):
    files = [f for f in os.listdir(folder) if f.endswith(".csv")]

    if not files:
        print(" No CSV files found in 'data' folder")
        exit()

    print("\n Available datasets:\n")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    return files


# -------------------------
#  Select dataset
# -------------------------
def select_dataset(files):
    while True:
        try:
            choice = int(input("\nEnter dataset number: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
            print(" Invalid choice")
        except ValueError:
            print(" Enter a valid number")


# -------------------------
#  Select target column
# -------------------------
def select_target(df):
    print("\n Columns:\n")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")

    while True:
        val = input("\nEnter target (name/index) or press Enter for auto: ").strip()

        if val == "":
            return None

        if val.isdigit():
            idx = int(val)
            if 1 <= idx <= len(df.columns):
                return df.columns[idx - 1]
            print(" Invalid index")

        else:
            cols_map = {c.lower(): c for c in df.columns}
            if val.lower() in cols_map:
                return cols_map[val.lower()]
            print(" Column not found")


# -------------------------
#  Main
# -------------------------
def main():
    files = list_datasets()
    selected_file = select_dataset(files)

    print(f"\n Selected: {selected_file}")

    df = load_data(os.path.join("data", selected_file))

    target_col = select_target(df)

    agent = DataAnalysisAgent(df, target_col)
    agent.run()


if __name__ == "__main__":
    main()
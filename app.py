import os
from src.data_loader import load_data
from src.agent import DataAnalysisAgent

# Get all CSV files
files = [f for f in os.listdir("data") if f.endswith(".csv")]

if not files:
    print("❌ No CSV files found in data folder")
    exit()

print("📂 Available datasets:\n")

for i, file in enumerate(files):
    print(f"{i}. {file}")

# ✅ SAFE INPUT LOOP
while True:
    try:
        choice = int(input("\n👉 Enter dataset number: "))

        if 0 <= choice < len(files):
            break
        else:
            print("❌ Invalid choice. Try again.")

    except ValueError:
        print("❌ Please enter a valid number.")

# ✅ Proceed only after valid input
file_path = os.path.join("data", files[choice])

print(f"\n📊 Selected dataset: {files[choice]}\n")

df = load_data(file_path)

agent = DataAnalysisAgent(df)
agent.run()
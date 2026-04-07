import pandas as pd

def load_data(path):
    # Try normal CSV
    df = pd.read_csv(path)
    
    # If only 1 column → wrong separator
    if df.shape[1] == 1:
        print("⚠️ Detected unusual format, trying alternative separator...")
        df = pd.read_csv(path, sep=';', decimal=',')
    
    # Drop empty columns
    df = df.dropna(axis=1, how='all')
    
    # Convert numeric columns
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass
    
    return df
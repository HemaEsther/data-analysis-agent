import pandas as pd
import csv


def load_data(path):
    try:
        # -------------------------
        # Detect delimiter
        # -------------------------
        with open(path, 'r', encoding='utf-8') as f:
            sample = f.read(1024)
            try:
                delimiter = csv.Sniffer().sniff(sample).delimiter
            except:
                delimiter = ','

        # -------------------------
        # Read CSV
        # -------------------------
        if delimiter == ';':
            df = pd.read_csv(path, sep=';', decimal=',')
        else:
            df = pd.read_csv(path, sep=delimiter)

        # -------------------------
        # Drop empty columns
        # -------------------------
        df = df.dropna(axis=1, how='all')

        # -------------------------
        # Clean & convert columns (single pass)
        # -------------------------
        for col in df.columns:
            if df[col].dtype == 'object':

                # Strip spaces
                df[col] = df[col].astype(str).str.strip()

                # Try numeric conversion
                temp = df[col].str.replace(',', '.', regex=False)
                converted = pd.to_numeric(temp, errors='coerce')

                if converted.notnull().sum() > 0.8 * len(df):
                    df[col] = converted
                    continue

                # Try date conversion
                if 'date' in col.lower():
                    df[col] = pd.to_datetime(df[col], errors='coerce')

        return df

    except FileNotFoundError:
        print(" File not found")
    except Exception as e:
        print(f" Error loading data: {e}")
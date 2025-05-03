import pandas as pd

def number_parquet_features(file_path):
    try:
        df = pd.read_parquet(file_path)
        print("Number of features (columns):", df.shape[1])
    except FileNotFoundError:
        print("File not found.")
# Example usage
file_path = r'C:\Users\DELL\Documents\Professional-Software-Engineering\PyThon\27063325-nishita\W3-5\Sample_data_2.parquet'  
number_parquet_features(file_path)

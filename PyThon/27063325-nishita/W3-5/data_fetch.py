import pandas as pd

csv_path = r"C:\Users\DELL\Documents\Professional-Software-Engineering\PyThon\27063325-nishita\W3-5\1026_Screen_Observations_daily.csv"
df = pd.read_csv(csv_path)

print(df.head())
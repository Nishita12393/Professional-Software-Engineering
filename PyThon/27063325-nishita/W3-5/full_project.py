import math
import pandas as pd


class ParquetFeatureCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_features(self):
        try:
            df = pd.read_parquet(self.file_path)
            print(f"[INFO] Number of features (columns): {df.shape[1]}")
        except FileNotFoundError:
            print("[ERROR] Parquet file not found. Please check the file path.")
        except Exception as e:
            print(f"[ERROR] Failed to read parquet file: {e}")


class UnderscoreCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def count_underscores(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                count = content.count('__')
                print(f"[INFO] Number of '__' in the file: {count}")
                return count
        except FileNotFoundError:
            print("[ERROR] Text file not found. Please check the file path.")
        except Exception as e:
            print(f"[ERROR] Failed to read text file: {e}")


class CSVPreviewer:
    def __init__(self, file_path):
        self.file_path = file_path

    def preview(self):
        try:
            df = pd.read_csv(self.file_path)
            print("[INFO] First 5 rows of the CSV file:")
            print(df.head())
        except FileNotFoundError:
            print("[ERROR] CSV file not found. Please check the file path.")
        except Exception as e:
            print(f"[ERROR] Failed to read CSV file: {e}")


class MathFunction:
    def _init_(self, angle_degrees):
        self.angle_degrees = angle_degrees
        self.angle_radian = math.radians(angle_degrees)

    def calculate_sin(self):
        return math.sin(self.angle_radians)

    def calculate_cos(self):
        return math.cos(self.angle_radians)

    def display_results(self):
        print(f"Sine({self.angle_degrees}°) = {self.calculate_sin()}")

        print(f"Cosine({self.angle_degrees}°) = {self.calculate_cos()}")
try:
    angle = float(input("Enter angle in degrees: "))
    calculator = MathFunction(angle)
    calculator.display_results()
except ValueError:
    print("Please enter a valid number.")  



def main():
    # File paths (replace with actual paths)
    parquet_file = r'C:\Users\DELL\Documents\Professional-Software-Engineering\PyThon\27063325-nishita\W3-5\Sample_data_2.parquet'
    txt_file = r'C:\Users\DELL\Documents\Professional-Software-Engineering\PyThon\27063325-nishita\W3-5\sample_text.txt'
    csv_file = r'C:\Users\DELL\Documents\Professional-Software-Engineering\PyThon\27063325-nishita\W3-5\sample_junk_mail.csv'

    print("\n=== Parquet File Feature Count ===")
    parquet_counter = ParquetFeatureCounter(parquet_file)
    parquet_counter.count_features()

    print("\n=== Underscore Count in TXT File ===")
    underscore_counter = UnderscoreCounter(txt_file)
    underscore_counter.count_underscores()

    print("\n=== CSV File Preview ===")
    csv_previewer = CSVPreviewer(csv_file)
    csv_previewer.preview()


if __name__ == "__main__":
    main()

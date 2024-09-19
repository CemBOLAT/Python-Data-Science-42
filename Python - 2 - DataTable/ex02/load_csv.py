import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    try:
        if (not path.endswith(".csv")):
            raise AssertionError("File is not a CSV file")
        with open(path) as csv_file:
            data_in_csv = pd.read_csv(csv_file)
            print(f"Loading dataset of dimensions {data_in_csv.shape}")
            return data_in_csv
    except FileNotFoundError:
        print(f"File not found: {path}")
    except PermissionError as e:
        print(f"Permission Error: {e}")
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    return None    
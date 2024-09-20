import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame

    Args:
        path (str): The path to the CSV file

    Returns:
        pd.DataFrame: The DF containing the data from the CSV file

    Raises:
        FileNotFoundError: If the file is not found
        PermissionError: If the file is not accessible
        AssertionError: If the file is not a CSV file
    """
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

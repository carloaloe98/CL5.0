import pandas as pd


def load_excel_file(file_path: str) -> pd.DataFrame:
    """
    Load an Excel file into a pandas DataFrame.
    :param file_path:
    :return:
    """
    try:
        df = pd.read_excel(file_path, dtype=str).fillna("")
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return pd.DataFrame()
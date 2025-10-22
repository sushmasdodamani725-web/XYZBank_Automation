# utils/data_reader.py
import pandas as pd

def read_excel(file_path, sheet_name=0):
    """Read test data from an Excel file."""
    return pd.read_excel(file_path, sheet_name=sheet_name)

def read_csv(file_path):
    """Read test data from a CSV file."""
    return pd.read_csv(file_path)

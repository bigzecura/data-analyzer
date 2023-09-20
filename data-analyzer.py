import pandas as pd
from io import StringIO

def read_csv_file(file_path):
    """
    Read CSV file and return a Pandas DataFrame.
    """
    return pd.read_csv(file_path)

def basic_data_analysis(data):
    """
    Perform basic data analysis on the DataFrame and return the results.
    """

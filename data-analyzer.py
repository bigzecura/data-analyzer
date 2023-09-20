import pandas as pd
from io import StringIO

def read_csv_file(file_path):
    """
    Read CSV file and return a Pandas DataFrame.
    """
    return pd.read_csv(file_path)
    results = {
        'number_of_rows': len(data),
        'number_of_columns': len(data.columns),
        'column_names': list(data.columns),
        'data_types': dict(data.dtypes),
        'missing_values': dict(data.isna().sum()),
        'descriptive_stats': data.describe(include='all').to_dict()
    }
    return results

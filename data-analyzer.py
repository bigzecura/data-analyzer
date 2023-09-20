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
    results = {
        'number_of_rows': len(data),
        'number_of_columns': len(data.columns),
        'column_names': list(data.columns),
        'data_types': dict(data.dtypes),
        'missing_values': dict(data.isna().sum()),
        'descriptive_stats': data.describe(include='all').to_dict()
    }
    return results

def generate_markdown_report(results):
    """
    Generate a summary report in Markdown format.
    """
    report = StringIO()
    report.write("# Data Analysis Report\n\n")

    report.write("## General Information\n\n")
    report.write(f"- Number of rows: {results['number_of_rows']}\n")
    report.write(f"- Number of columns: {results['number_of_columns']}\n")
    report.write(f"- Column names: {', '.join(results['column_names'])}\n\n")

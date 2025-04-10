"""
read_csv_data.py
Utility to read login test data from a CSV file.
"""

import csv
import os


def get_login_data(file_path):
    """
    Reads login credentials from a CSV file and returns a list of (username, password) tuples.
    """
    data_list = []
    full_path = os.path.abspath(file_path)

    try:
        with open(full_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_list.append((row['username'], row['password']))
    except FileNotFoundError:
        raise Exception(f"CSV file not found at path: {full_path}")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")

    return data_list

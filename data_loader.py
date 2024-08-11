# data_loader.py

import pandas as pd

def load_data(file_path):
        try:
            data = pd.read_csv('Student Mental health.csv')
            print("Data loaded successfully!")
            return data
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except pd.errors.EmptyDataError:
            print("No data found. The file is empty.")
        except Exception as e:
            print(f"An error occurred: {e}")
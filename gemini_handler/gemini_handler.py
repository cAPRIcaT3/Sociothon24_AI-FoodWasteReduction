import pandas as pd


class GeminiHandler:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_inventory_data_from_excel(self, file_path):
        try:
            # Load Excel file into a DataFrame
            data = pd.read_excel(file_path)

            # Check for missing or incorrect data
            if data.isnull().values.any():
                print("Warning: The Excel file contains missing values. Please check your file.")
                print("Missing values:\n", data.isnull().sum())

            # Convert 'Expiration Date' to datetime
            if 'Expiration Date' in data.columns:
                data['Expiration Date'] = pd.to_datetime(data['Expiration Date'], errors='coerce')
                if data['Expiration Date'].isnull().any():
                    print("Warning: Some 'Expiration Date' values could not be parsed.")
            else:
                print("Error: 'Expiration Date' column is missing from the Excel file.")
                return None

            # Calculate 'Days Remaining' for each item
            current_date = pd.Timestamp.now()
            data['Days Remaining'] = (data['Expiration Date'] - current_date).dt.days

            # Return cleaned DataFrame
            return data
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

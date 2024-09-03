import os
import pandas as pd

class DataLoader:
    def __init__(self, base_path):
        self.base_path = base_path
        self.yfinance_data_folder = os.path.join(self.base_path, 'yfinance_data')
        self.analyst_ratings_path = os.path.join(self.base_path, 'raw_analyst_ratings.csv/raw_analyst_ratings.csv')

    def load_yfinance_data(self):
        """Loads all CSV files in the yfinance_data folder and concatenates them into a single DataFrame."""
        dataframes = []
        if not os.path.exists(self.yfinance_data_folder):
            print(f"Directory not found: {self.yfinance_data_folder}")
            return pd.DataFrame()

        for filename in os.listdir(self.yfinance_data_folder):
            if filename.endswith('.csv'):
                file_path = os.path.join(self.yfinance_data_folder, filename)
                try:
                    df = pd.read_csv(file_path)
                    df['source_file'] = filename  # Add a column to identify the source of the data
                    dataframes.append(df)
                except Exception as e:
                    print(f"Failed to load {file_path}: {e}")
            else:
                print(f"Skipped non-CSV file: {filename}")

        if dataframes:
            return pd.concat(dataframes, ignore_index=True)
        else:
            print("No CSV files found in the yfinance_data folder.")
            return pd.DataFrame()

    def load_analyst_ratings(self):
        """Loads the raw analyst ratings CSV file."""
        if os.path.exists(self.analyst_ratings_path):
            try:
                return pd.read_csv(self.analyst_ratings_path)
            except Exception as e:
                print(f"Failed to load {self.analyst_ratings_path}: {e}")
                return pd.DataFrame()
        else:
            print(f"File not found: {self.analyst_ratings_path}")
            return pd.DataFrame()

    def load_data(self):
        """Loads both the Yahoo Finance data and the analyst ratings, returning them as a dictionary."""
        yfinance_data = self.load_yfinance_data()
        analyst_ratings = self.load_analyst_ratings()

        # Log the sizes of the dataframes
        print(f"Loaded Yahoo Finance data with {yfinance_data.shape[0]} rows and {yfinance_data.shape[1]} columns.")
        print(f"Loaded Analyst Ratings data with {analyst_ratings.shape[0]} rows and {analyst_ratings.shape[1]} columns.")

        return {
            'yfinance_data': yfinance_data,
            'analyst_ratings': analyst_ratings
        }

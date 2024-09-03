# src/data_loader.py

import pandas as pd

class DataLoader:
    def __init__(self, analyst_ratings_path, yfinance_data_path):
        self.analyst_ratings_path = analyst_ratings_path
        self.yfinance_data_path = yfinance_data_path
    
    def load_analyst_ratings(self):
        return pd.read_csv(self.analyst_ratings_path)
    
    def load_yfinance_data(self):
        return pd.read_csv(self.yfinance_data_path)

# Example usage
loader = DataLoader('c:/Users/user/Documents/10acadamy/week1_Data/raw_analyst_ratings.csv/raw_analyst_ratings.csv', 'c:/Users/user/Documents/10acadamy/week1_Data/yfinance_data/yfinance_data.csv')
analyst_data = loader.load_analyst_ratings()
yfinance_data = loader.load_yfinance_data()



            
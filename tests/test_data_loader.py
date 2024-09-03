import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_loader import DataLoader

def main():
    # Define the path to the data folder
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    # Initialize DataLoader with the base path
    loader = DataLoader(base_path)
    
    # Load the data
    data = loader.load_data()
    
    # Check and print the loaded data
    if 'yfinance_data' in data and not data['yfinance_data'].empty:
        print("YFinance Data (First 5 rows):")
        print(data['yfinance_data'].head())
    else:
        print("No Yahoo Finance data loaded or data is empty.")
    
    if 'analyst_ratings' in data and not data['analyst_ratings'].empty:
        print("\nAnalyst Ratings Data (First 5 rows):")
        print(data['analyst_ratings'].head())
    else:
        print("No Analyst Ratings data loaded or data is empty.")

if __name__ == "__main__":
    main()

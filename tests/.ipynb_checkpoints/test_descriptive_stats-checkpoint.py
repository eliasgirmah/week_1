# tests/test_descriptive_stats.py

import sys
import os
import pandas as pd

# Adjust the path to import from src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from descriptive_stats import DescriptiveStats

def test_descriptive_stats():
    # Define the path to the CSV file
    #test_data_path = os.path.join('data', 'AAPL_historical_data.csv')
    test_data_path = os.path.join('data', 'yfinance_data', 'AAPL_historical_data.csv')

    # Check if the file exists
    if not os.path.exists(test_data_path):
        print(f"Test file not found: {test_data_path}")
        return
    
    # Load the test data
    df = pd.read_csv(test_data_path)
    
    # Initialize the DescriptiveStats object
    stats = DescriptiveStats(df)
    
    # Get and print summary statistics
    summary_stats = stats.get_summary_statistics()
    print("Summary Statistics:")
    print(summary_stats.head())  # Print first few rows for brevity
    
    # Get and print missing values
    missing_values = stats.get_missing_values()
    print("\nMissing Values:")
    print(missing_values)
    
    # Get and print data types
    data_types = stats.get_data_types()
    print("\nData Types:")
    print(data_types)
    
    # Get and print correlation matrix
    correlations = stats.get_correlations()
    print("\nCorrelation Matrix:")
    print(correlations)

if __name__ == "__main__":
    test_descriptive_stats()

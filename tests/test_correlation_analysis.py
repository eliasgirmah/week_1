import sys
import os
import pandas as pd

# Adjust the path to include the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from correlation_analysis import CorrelationAnalysis

def test_correlation_analysis():
    # Load sample data
    test_data_path = 'data/yfinance_data/AAPL_historical_data.csv'
    dataframe = pd.read_csv(test_data_path)
    
    # Instantiate the CorrelationAnalysis class
    correlation_analysis = CorrelationAnalysis(dataframe)
    
    # Calculate correlation matrix
    correlation_matrix = correlation_analysis.calculate_correlation()
    print("Correlation Matrix:")
    print(correlation_matrix)
    
    # Plot correlation heatmap
    correlation_analysis.plot_correlation_heatmap(correlation_matrix)

if __name__ == "__main__":
    test_correlation_analysis()

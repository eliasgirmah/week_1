import os
from src.data_loader import DataLoader
from src.descriptive_stats import DescriptiveStats
from src.text_analysis import TextAnalysis
from src.time_series_analysis import TimeSeriesAnalysis
from src.correlation_analysis import CorrelationAnalysis

# Define paths
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'yfinance_data')
analyst_ratings_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'raw_analyst_ratings.csv')

# Load data
loader = DataLoader(yfinance_data_dir=data_dir, analyst_ratings_path=analyst_ratings_path)
all_yfinance_data = loader.load_yfinance_data()
analyst_ratings_df = loader.load_analyst_ratings()

# Descriptive statistics
descriptive_stats = DescriptiveStats(analyst_ratings_df)
print("Headline Length Stats:")
print(descriptive_stats.headline_length_stats())
print("\nArticles Per Publisher:")
print(descriptive_stats.articles_per_publisher())
print("\nPublication Dates Analysis:")
print(descriptive_stats.publication_dates_analysis())

# Text Analysis
headlines = analyst_ratings_df['headline'].tolist()
text_analysis = TextAnalysis(headlines)
print("\nSentiment Analysis Results:")
print(text_analysis.sentiment_analysis())
print("\nTopic Modeling Results:")
print(text_analysis.topic_modeling())

# Time Series Analysis
time_series_analysis = TimeSeriesAnalysis(analyst_ratings_df)
print("\nPublication Frequency:")
print(time_series_analysis.publication_frequency())
print("\nTime of Day Analysis:")
print(time_series_analysis.time_of_day_analysis())

# Correlation Analysis
for symbol in all_yfinance_data.keys():
    correlation_analysis = CorrelationAnalysis(sentiment_df=text_analysis.sentiment_analysis(), stock_data=all_yfinance_data)
    correlation = correlation_analysis.correlate_sentiment_and_stock(symbol)
    print(f"\nCorrelation between sentiment and stock price for {symbol}: {correlation}")

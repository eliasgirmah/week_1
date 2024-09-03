# tests/test_text_analysis.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from text_analysis import TextAnalysis

import pandas as pd


def test_text_analysis():
    test_data_path = os.path.join('data', 'raw_analyst_ratings.csv/raw_analyst_ratings.csv')
    dataframe = pd.read_csv(test_data_path)
    
    text_analysis = TextAnalysis(dataframe)
    text_analysis.clean_text('headline')
    
    # Get common bigrams
    common_phrases = text_analysis.get_common_phrases('headline', ngram_range=(2, 2), n=10)
    
    # Printing all top 10 common phrases
    print("Top 10 Common Phrases:")
    for phrase, count in common_phrases:
        print(f"{phrase}: {count}")

if __name__ == "__main__":
    test_text_analysis()
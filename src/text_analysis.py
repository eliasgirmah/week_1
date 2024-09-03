# src/text_analysis.py

import pandas as pd
from collections import Counter
import re
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

class TextAnalysis:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def clean_text(self, column_name):
        self.dataframe[column_name] = self.dataframe[column_name].str.lower().str.replace(r'\W+', ' ', regex=True)
        return self.dataframe[column_name]

    def get_common_phrases(self, column_name, ngram_range=(1, 1), n=10):
        vectorizer = CountVectorizer(ngram_range=ngram_range, max_features=10000)
        ngrams = vectorizer.fit_transform(self.dataframe[column_name])
        
        # Use sparse matrix format without converting to a dense array
        ngram_counts = Counter(dict(zip(vectorizer.get_feature_names_out(), ngrams.sum(axis=0).A1)))
        
        return ngram_counts.most_common(n)
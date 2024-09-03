# src/descriptive_stats.py

import pandas as pd

class DescriptiveStats:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_summary_statistics(self):
        return self.dataframe.describe()

    def get_missing_values(self):
        return self.dataframe.isna().sum()

    def get_data_types(self):
        return self.dataframe.dtypes

    def get_correlations(self):
        # Select only numeric columns for correlation analysis
        numeric_df = self.dataframe.select_dtypes(include=['number'])
        return numeric_df.corr()

    def analyze_textual_lengths(self, text_column):
        """Analyze the lengths of textual data in a specified column."""
        if text_column not in self.dataframe.columns:
            raise ValueError(f"Column {text_column} does not exist in the DataFrame.")
        # Calculate lengths of text in the specified column
        self.dataframe[f'{text_column}_length'] = self.dataframe[text_column].astype(str).apply(len)
        return self.dataframe[[text_column, f'{text_column}_length']].describe()

    def count_articles_per_publisher(self, publisher_column):
        """Count the number of articles per publisher."""
        if publisher_column not in self.dataframe.columns:
            raise ValueError(f"Column {publisher_column} does not exist in the DataFrame.")
        return self.dataframe[publisher_column].value_counts()

    def analyze_publication_dates(self, date_column):
        """Analyze publication dates to see trends over time."""
        if date_column not in self.dataframe.columns:
            raise ValueError(f"Column {date_column} does not exist in the DataFrame.")
        # Convert to datetime if not already
        self.dataframe[date_column] = pd.to_datetime(self.dataframe[date_column], errors='coerce')
        # Extract date parts and count occurrences
        return self.dataframe[date_column].dt.to_period('D').value_counts().sort_index()

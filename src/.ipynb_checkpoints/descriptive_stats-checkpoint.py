import pandas as pd

class DescriptiveStats:
    def __init__(self, df):
        self.df = df

    def headline_length_stats(self):
        """Calculates and returns basic statistics for the headline lengths."""
        self.df['headline_length'] = self.df['headline'].apply(len)
        return self.df['headline_length'].describe()

    def articles_per_publisher(self):
        """Counts the number of articles per publisher."""
        return self.df['publisher'].value_counts()

    def publication_date_trends(self):
        """Analyzes and returns publication date trends."""
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['publication_date'] = self.df['date'].dt.date
        return self.df['publication_date'].value_counts().sort_index()

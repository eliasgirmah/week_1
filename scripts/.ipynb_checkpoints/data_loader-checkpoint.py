import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Loads the dataset from the given file path."""
        df = pd.read_csv(self.file_path)
        return df

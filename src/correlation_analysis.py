import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class CorrelationAnalysis:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def calculate_correlation(self, method='pearson'):
        # Filter out non-numeric columns
        numeric_dataframe = self.dataframe.select_dtypes(include=[np.number])
        return numeric_dataframe.corr(method=method)

    def plot_correlation_heatmap(self, correlation_matrix):
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.show()

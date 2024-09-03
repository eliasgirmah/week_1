# Financial Data Analysis Project

This project is designed to perform various analyses on financial news and stock price data, including sentiment analysis, correlation analysis, and time series analysis. The project is structured with modular Python scripts and can be used in Jupyter Notebooks for interactive data analysis.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
  - [Data Loading](#data-loading)
  - [Descriptive Statistics](#descriptive-statistics)
  - [Text Analysis](#text-analysis)
  - [Correlation Analysis](#correlation-analysis)
  - [Time Series Analysis](#time-series-analysis)
- [Testing](#testing)
- [Jupyter Notebooks](#jupyter-notebooks)
- [License](#license)

## Project Structure

The project is organized into the following directories:

. ├── data/ # Data directory containing CSV files │ ├── yfinance_data/ # Yahoo Finance data CSV files │ └── raw_analyst_ratings.csv # Analyst ratings CSV file ├── src/ # Source code directory │ ├── data_loader.py # Data loading class │ ├── descriptive_stats.py # Descriptive statistics class │ ├── text_analysis.py # Text analysis class │ ├── correlation_analysis.py # Correlation analysis class │ └── time_series_analysis.py # Time series analysis class ├── tests/ # Unit tests directory │ ├── test_data_loader.py # Tests for DataLoader │ ├── test_descriptive_stats.py # Tests for DescriptiveStats │ ├── test_text_analysis.py # Tests for TextAnalysis │ ├── test_correlation_analysis.py # Tests for CorrelationAnalysis │ └── test_time_series_analysis.py # Tests for TimeSeriesAnalysis └── notebooks/ # Jupyter Notebooks directory ├── data_loading.ipynb # Notebook for data loading ├── descriptive_stats.ipynb # Notebook for descriptive statistics ├── text_analysis.ipynb # Notebook for text analysis ├── correlation_analysis.ipynb # Notebook for correlation analysis └── time_series_analysis.ipynb # Notebook for time series analysis



## Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip (Python package installer)**
- **Jupyter Notebook** (optional, for interactive analysis)
- **VS Code Extensions**:
  - Python
  - Jupyter

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/eliasgirmah/week1
   cd week1

2. Install required Python packages:
    pip install -r requirements.txt

3. Place your data:

	Place your Yahoo Finance data CSV files in the data/yfinance_data/ directory.
	Place your analyst ratings CSV file as data/raw_analyst_ratings.csv.
4. Install required Python packages:
     pip install -r requirements.txt
5. Usage
Data Loading
Use the data_loader.py script or the data_loading.ipynb notebook to load your financial data.

Descriptive Statistics
Analyze your data's basic statistics using descriptive_stats.py or the descriptive_stats.ipynb notebook.

Text Analysis
Perform sentiment and text analysis using text_analysis.py or the text_analysis.ipynb notebook.

Correlation Analysis
Explore correlations between different data variables with correlation_analysis.py or the correlation_analysis.ipynb notebook.

Time Series Analysis
Analyze trends over time using time_series_analysis.py or the time_series_analysis.ipynb notebook.

Testing
Run unit tests located in the tests/ directory to ensure your code is functioning as expected.

Jupyter Notebooks
Use the notebooks in the notebooks/ directory for interactive data analysis.

License
This project is licensed under the 10 Academy License.
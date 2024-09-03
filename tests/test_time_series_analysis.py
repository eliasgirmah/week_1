import unittest
import pandas as pd
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from time_series_analysis import TimeSeriesAnalysis

class TestTimeSeriesAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = {
            'date': ['2024-08-01', '2024-08-02', '2024-08-03'],
            'headline': ['Stock hits new high', 'Company reports earnings', 'Market crashes']
        }
        cls.df = pd.DataFrame(data)
        cls.df['date'] = pd.to_datetime(cls.df['date'])
        cls.time_series_analysis = TimeSeriesAnalysis(cls.df)
        
    def test_publication_frequency(self):
        frequency = self.time_series_analysis.publication_frequency()
        self.assertEqual(len(frequency), 3, "Publication frequency analysis should have three entries")

    def test_time_of_day_analysis(self):
        cls.df['time'] = pd.to_datetime(cls.df['date']).dt.time
        time_of_day_analysis = self.time_series_analysis.time_of_day_analysis()
        self.assertIn(pd.Timestamp.now().time(), time_of_day_analysis.index, "Time of day analysis has incorrect data")

if __name__ == '__main__':
    unittest.main()

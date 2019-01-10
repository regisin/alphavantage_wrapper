import unittest
from alphavantage_wrapper.AlphaVantage import AlphaVantage

"""Tests will only work if the remote API is also working, will fail if no internet connection"""
class TestAlphaVantage(unittest.TestCase):
    def setUp(self):
        api_key = 'demo'
        self.av = AlphaVantage(api_key)

    def test_intraday(self):
        self.av.get_time_series_intraday('MSFT', '5min')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo')
        info = self.av._current_meta['1. Information']
        symb = self.av._current_meta['2. Symbol']
        intv = self.av._current_meta['4. Interval']
        outp = self.av._current_meta['5. Output Size']
        self.assertEqual(info, "Intraday (5min) open, high, low, close prices and volume")
        self.assertEqual(symb, "MSFT")
        self.assertEqual(intv, "5min")
        self.assertEqual(outp, "Compact")

    def test_daily(self):
        self.av.get_time_series_daily('MSFT')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo')
        info = self.av._current_meta['1. Information']
        symb = self.av._current_meta['2. Symbol']
        outp = self.av._current_meta['4. Output Size']
        self.assertEqual(info, "Daily Prices (open, high, low, close) and Volumes")
        self.assertEqual(symb, "MSFT")
        self.assertEqual(outp, "Compact")

    def test_daily_adjusted(self):
        self.av.get_time_series_daily_adjusted('MSFT')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&apikey=demo')
        info = self.av._current_meta['1. Information']
        symb = self.av._current_meta['2. Symbol']
        outp = self.av._current_meta['4. Output Size']
        self.assertEqual(info, "Daily Time Series with Splits and Dividend Events")
        self.assertEqual(symb, "MSFT")
        self.assertEqual(outp, "Compact")

    def test_weekly(self):
        self.av.get_time_series_weekly('MSFT')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MSFT&apikey=demo')
        info = self.av._current_meta['1. Information']
        symb = self.av._current_meta['2. Symbol']
        self.assertEqual(info, "Weekly Prices (open, high, low, close) and Volumes")
        self.assertEqual(symb, "MSFT")

    def test_weekly_adjusted(self):
        self.av.get_time_series_weekly_adjusted('MSFT')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=MSFT&apikey=demo')
        info = self.av._current_meta['1. Information']
        symb = self.av._current_meta['2. Symbol']
        self.assertEqual(info, "Weekly Adjusted Prices and Volumes")
        self.assertEqual(symb, "MSFT")

    def test_monthly(self):
        self.av.get_time_series_monthly('MSFT')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MSFT&apikey=demo')
        info = self.av._current_meta['1. Information']
        symb = self.av._current_meta['2. Symbol']
        self.assertEqual(info, "Monthly Prices (open, high, low, close) and Volumes")
        self.assertEqual(symb, "MSFT")

    def test_monthly_adjusted(self):
        self.av.get_time_series_monthly_adjusted('MSFT')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=MSFT&apikey=demo')
        info = self.av._current_meta['1. Information']
        symb = self.av._current_meta['2. Symbol']
        self.assertEqual(info, "Monthly Adjusted Prices and Volumes")
        self.assertEqual(symb, "MSFT")

    def test_quote_endpoint(self):
        self.av.get_global_quote('MSFT')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=demo')
        self.assertIn("01. symbol", self.av._current_meta.keys())
        self.assertIn("02. open", self.av._current_meta.keys())
        self.assertIn("03. high", self.av._current_meta.keys())
        self.assertIn("04. low", self.av._current_meta.keys())
        self.assertIn("05. price", self.av._current_meta.keys())
        self.assertIn("06. volume", self.av._current_meta.keys())
        self.assertIn("07. latest trading day", self.av._current_meta.keys())
        self.assertIn("08. previous close", self.av._current_meta.keys())
        self.assertIn("09. change", self.av._current_meta.keys())
        self.assertIn("10. change percent", self.av._current_meta.keys())

    def test_search_endpoint(self):
        self.av.get_symbol_search('Micro')
        self.assertEqual(self.av._current_cmd, 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=Micro&apikey=demo')
        self.assertEqual(len(self.av._current_meta), 10)

if __name__ == '__main__':
    unittest.main()
import requests
import pandas as pd

class AlphaVantage():
    def __init__(self, api_key, base_url=f'https://www.alphavantage.co/query?'):
        self._api_key=api_key
        self.base_url = base_url
        # Available API functions (only the implemented ones are listed here)
        self.TIME_SERIES_INTRADAY = 'TIME_SERIES_INTRADAY'
        self.TIME_SERIES_DAILY = 'TIME_SERIES_DAILY'
        self.TIME_SERIES_DAILY_ADJUSTED = 'TIME_SERIES_DAILY_ADJUSTED'
        self.TIME_SERIES_WEEKLY = 'TIME_SERIES_WEEKLY'
        self.TIME_SERIES_WEEKLY_ADJUSTED = 'TIME_SERIES_WEEKLY_ADJUSTED'
        self.TIME_SERIES_MONTHLY = 'TIME_SERIES_MONTHLY'
        self.TIME_SERIES_MONTHLY_ADJUSTED = 'TIME_SERIES_MONTHLY_ADJUSTED'
        self.GLOBAL_QUOTE = 'GLOBAL_QUOTE'
        self.SYMBOL_SEARCH = 'SYMBOL_SEARCH'

    def _append_key(self, cmd):
        a = 'apikey=%s&' % self._api_key
        return cmd + a
    
    def _append_param(self, cmd, key, value):
        a = '%s=%s&' % (key, value)
        return cmd + a

    def get_time_series_intraday(self, ticker, interval, outputsize='compact', datatype='json'):
        """
        
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.TIME_SERIES_INTRADAY)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'interval', interval)
        cmd = self._append_param(cmd, 'outputsize', size)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Time Series (%s)' % interval], orient='index')
        return df

    def get_time_series_daily(self, ticker, outputsize='compact', datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.TIME_SERIES_DAILY)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'outputsize', outputsize)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Time Series (Daily)'], orient='index')
        return df

    def get_time_series_daily_adjusted(self, ticker, outputsize='compact', datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.TIME_SERIES_DAILY_ADJUSTED)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'outputsize', outputsize)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Time Series (Daily)'], orient='index')
        return df

    def get_time_series_weekly(self, ticker, datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.TIME_SERIES_WEEKLY)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Weekly Time Series'], orient='index')
        return df

    def get_time_series_weekly_adjusted(self, ticker, datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.TIME_SERIES_WEEKLY_ADJUSTED)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Weekly Adjusted Time Series'], orient='index')
        return df

    def get_time_series_monthly(self, ticker, datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.TIME_SERIES_MONTHLY)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Monthly Time Series'], orient='index')
        return df

    def get_time_series_monthly_adjusted(self, ticker, datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.TIME_SERIES_MONTHLY_ADJUSTED)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Monthly Adjusted Time Series'], orient='index')
        return df

    def get_global_quote(self, ticker, datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.GLOBAL_QUOTE)
        cmd = self._append_param(cmd, 'symbol', ticker)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['Global Quote'], orient='index')
        return df

    def get_symbol_search(self, keyword, datatype='json'):
        """
        """
        cmd = self.base_url
        cmd = self._append_key(cmd)
        cmd = self._append_param(cmd, 'function', self.GLOBAL_QUOTE)
        cmd = self._append_param(cmd, 'keywords', ticker)
        cmd = self._append_param(cmd, 'datatype', 'json')
        content_dict = requests.get(cmd).json()
        df = pd.DataFrame.from_dict(content_dict['bestMatches'], orient='index')
        return df

    def get(self, ticker, size='full'):
        """
        This is simply a 'middleware' that formats results to be as similar to that of 'quandl.get()'
        Some columns do not exist in alpha: Adj. Open, Adj. High, Adj. Low, Adj. Volume.
        TO-DO: compute missing columns (need to use dividend and split ratio).
        """
        df = self.get_time_series_daily_adjusted(ticker, size=size)
        # To keep consistent with quandl format, add/change column names and index
        df.index.rename('Date', inplace=True)
        df.rename(columns={
            '1. open': 'Open',
            '2. high': 'High', 
            '3. low': 'Low', 
            '4. close': 'Close', 
            '5. adjusted close': 'Adj. Close', 
            '6. volume': 'Volume',
            '7. dividend amount': 'Ex-Dividend',
            '8. split coefficient': 'Split Ratio'
            }, inplace=True)
        # Convert to the appropriate format (i.e. as similar to quandl as possible)
        df.index = pd.to_datetime(df.index)
        df['Open'] = pd.to_numeric(df['Open'])
        df['High'] = pd.to_numeric(df['High'])
        df['Low'] = pd.to_numeric(df['Low'])
        df['Close'] = pd.to_numeric(df['Close'])
        df['Adj. Close'] = pd.to_numeric(df['Adj. Close'])
        df['Volume'] = pd.to_numeric(df['Volume'])
        df['Ex-Dividend'] = pd.to_numeric(df['Ex-Dividend'])
        df['Split Ratio'] = pd.to_numeric(df['Split Ratio'])
        # For now just copy, might need to be a formula if split/dividend are different
        df['Adj. Open'] = df['Open']
        return df

# Introduction

This is a simple wrapper for the [Alpha Vantage API](https://www.alphavantage.co). Since `quandl` disabled the free `WIKI` data source, I created this package that uses Alpha instead.

All results are converted to a `pandas`'s `DataFrame` to make data manipulation/computation/etc. faster.

# Install

You can install this package globally with:

```
pip install alphavantage_wrapper pandas
```

Or if you do not want to install globally, but on a per project basis for example, you can clone this repo (you will still need `pandas` package):

```
cd my-awesome-project
git clone http://github.com/regisin/alphavantage-wrapper
```

Tested using `Python 3`.

# Usage

```python
from alphavantage_wrapper import AlphaVantage
import pandas as pd

api_key = 'APIKeyGoesHere'

av = AlphaVantage(api_key)

# The company's stock symbol (ex.: Microsoft)
ticker = 'MSFT'
# Retrieval the 100 most recent financial data (daily time series, adjusted)
stock = av.get_time_series_daily_adjusted(ticker)
# do stuff with data
print(stock)
```

# Changelog

* v0.0.3
* v0.0.2
  * Bug fixes

* v0.0.1
  * First commit
  * Include LICENSE file
  * Include README
  * Implemented all time series functions as seen in https://www.alphavantage.co/documentation

# TO-DO

* For v0.1.0

- [ ] Improve source-code comments (function descriptions, add example)
- [ ] Time series example script
- [ ] Implement Forex functions
- [ ] Implement Cryptocurrencies functions
- [ ] Implement Technical Indicators functions
- [ ] Implement Sector Performances functions
- [ ] Add unit tests
- [ ] Add CSV support, maybe?

* For v0.0.1

- [x] Create package structure
- [x] Write readme
- [x] Implement time series API functions
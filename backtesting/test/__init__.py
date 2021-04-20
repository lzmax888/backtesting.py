"""Data and utilities for testing."""
import pandas as pd

import pandas_ta as ta


def _read_file(filename):
    from os.path import dirname, join

    return pd.read_csv(join(dirname(__file__), filename),
                       index_col=0, parse_dates=True, infer_datetime_format=True)


GOOG = _read_file('GOOG.csv')
"""DataFrame of daily NASDAQ:GOOG (Google/Alphabet) stock price data from 2004 to 2013."""

EURUSD = _read_file('EURUSD.csv')
"""DataFrame of hourly EUR/USD forex data from April 2017 to February 2018."""


def SMA(arr: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return pd.Series(arr).rolling(n).mean()


'''
sma10 = ta.sma(df["Close"], length=10)
Returns a Series with name: SMA_10
donchiandf = ta.donchian(df["HIGH"], df["low"], lower_length=10, upper_length=15)
Returns a DataFrame named DC_10_15 and column names: DCL_10_15, DCM_10_15, DCU_10_15
ema10_ohlc4 = ta.ema(ta.ohlc4(df["Open"], df["High"], df["Low"], df["Close"]), length=10)
Chaining indicators is possible but you have to be explicit.
Since it returns a Series named EMA_10. If needed, you may need to uniquely name it.
'''

def HMA(arr: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return ta.hma(pd.Series(arr),n)


def EMA(arr: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return ta.ema(pd.Series(arr),n)
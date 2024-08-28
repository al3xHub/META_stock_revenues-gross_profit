import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
from datetime import datetime
yf.pdr_override()
ticker="ITX"
start=datetime(2023,1,1)
ends=datetime(2023,11,1)
data=pdr.get_data_yahoo(ticker,start,ends)
print(data)


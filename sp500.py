from yahoo_fin import stock_info as si
import pandas as pd

ticker=si.tickers_sp500()
df=pd.DataFrame(ticker)

for i in ticker:
    data=si.get_data(i, start_date="2023-01-01", end_date="2023-11-01")
    data['Ticker'] = i
    df=pd.concat([df, data])
    print(i)

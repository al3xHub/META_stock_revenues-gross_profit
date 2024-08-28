import requests
import pandas as pd

'''
for free:
income-statement, balance-sheet-statement, cash-flow-statement, income-statement-growth, balance-sheet-statement-growth,
cash-flow-statement-growth, ratios-ttm, ratios, financial-statement-growth, key-metrics, enterprise-values, key-metrics-ttm, rating,
historical-rating, discounted-cash-flow, historical-discounted-cash-flow-statement, historical-chart/1m
'''




base='https://financialmodelingprep.com/api'
type='income-statement'
symbol='AAPL'
apikey='AIfHsoPgJJM70JcOdz61DDYHWDeo1gAD'
url=f'{base}/v3/{type}/{symbol}?period=annual&apikey={apikey}'

# print(url)

response=requests.get(url)
data=response.json()
df=pd.DataFrame(data).T


# descargar df en csv
df.to_csv('./aapl.csv')


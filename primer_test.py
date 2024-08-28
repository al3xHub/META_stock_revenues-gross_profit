import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt

# indices = pd.read_html("http://finance.yahoo.com/world-indices")[0]
# indices_symbol= indices['Symbol'].values.tolist()

# imprime indices bursalites
# print(indices_symbol)

# ibm=yf.Ticker("IBM")
# print(ibm.history(period="max"))
# print(ibm.get_info())

# #cambia el comportamiento de la libreria pandas_datareader para que use la libreria yfinance.
# yf.pdr_override()

# # definir lista de tickers
tickers = ['NFLX']

# # importar modulo datetime para manejar fechas y horas
from datetime import datetime

# # fechas de inicio y fin 
inicio=datetime(2020,1,1)
fin=datetime(2023,1,1)

# # obtener datos de los tickers
datos=pdr.get_data_yahoo(tickers,inicio,fin)
print(datos)

# data= yf.download('EPAM',start='2020-01-01', end= '2023-11-01')
# print(data)
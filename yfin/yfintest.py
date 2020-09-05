import yfinance as yf
from yfinance import Ticker

stock_ticker = 'AAPL'

ticker = yf.Ticker(stock_ticker)

df = (ticker.info)
print(type(df))
for items in df:
    print(df.itervalues())


# print(ticker.options)
# print(ticker.balance_sheet)

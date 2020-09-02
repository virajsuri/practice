import yfinance as yf
from yfinance import Ticker

stock_ticker = 'AAPL'

ticker = yf.Ticker(stock_ticker)

pp = ticker.info
print(pp)
# print(ticker.balance_sheet)

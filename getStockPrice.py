import openpyxl as xl
import yfinance as yf

def getStockPrice(name):
    stock = yf.Ticker(name)
    closingPrice = stock.history()
    print(name)
    print(closingPrice['Close'][len(closingPrice)-1])


getStockPrice("MSFT")
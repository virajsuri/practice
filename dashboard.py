import yfinance as yf
from yfinance import Ticker
from pprint import pprint

from finnews.client import News

def getStockPrice(name):
    #returns O/H/L/C/Volume/Divs/Stock Splits

    stock = yf.Ticker(name)
    closingPrice = stock.history(period="2d")
    return closingPrice

def get_current_price(ticker):
    close = getStockPrice(ticker)['Close']
    close_pct_1d = (close[1]-close[0])/close[0]
    curr_price = close[1]
    return (ticker+": "+str(curr_price)+" ("+str('{:.1%}'.format(close_pct_1d))+")")

spy_price = get_current_price('SPY')
dow_price = get_current_price('^DJI')
nasdaq_price = get_current_price('^IXIC')
russel_price = get_current_price('^RUT')
print()
five_yr = get_current_price('^FVX')
ten_yr = get_current_price('^TNX')
thirty_year = get_current_price('^TYX')

print()

news_client = News()
wsj_client = news_client.wsj
wsj_bus = wsj_client.us_business_news()
for articles in wsj_bus:
    print(articles['title'])
    # print(articles['link'])

from pandas_datareader import data as pdr
import datetime
import bs4 as bs
import pickle
import requests
import yfinance as yf

    
def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    return tickers




# date = datetime.datetime.strptime(date, "%m/%d/%Y")
date = datetime.date.today()
print(date)
print(date-1)

stockTickers = save_sp500_tickers()

# print(stockTickers)

for x in range(len(stockTickers)):
    print(stockTickers[x])
    tickerSymbol = stockTickers[x]
    closePrice = yf.download(tickerSymbol, datetime.today()-1, datetime.today(), progress=false)
    print(closePrice)
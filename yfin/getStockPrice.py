import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def getStockPrice(name):
    #returns O/H/L/C/Volume/Divs/Stock Splits

    stock = yf.Ticker(name)
    closingPrice = stock.history(period="ytd")
    return closingPrice

def plotGraph(outputTable, field):
    print("Plotting graph")
    fig, (ax1, ax2) = plt.subplots(2)
    # plt.xkcd()

    ax1.plot(outputTable[field], color='black',linestyle='solid')
    ax2.plot(outputTable['Volume'], color='red',linestyle='solid')

    scale_y = 1e6
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_y)))

    ax1.set_title(field)
    ax2.set_title('Volume')    

    ax2.set_ylabel('Volume in millions')

    plt.tight_layout()
    plt.show()


field = 'Close'
ticker = 'CRM'
stockInfo = getStockPrice(ticker) 
plotGraph(stockInfo, field)

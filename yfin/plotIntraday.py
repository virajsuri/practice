import matplotlib.pyplot as plt
import yfinance as yf
import datetime

def plotGraph(prices):
    print("Plotting graph")
    figure, axes = plt.subplots(figsize=(10, 6)) 
    # plt.figure(figsize=(10,4))
    plt.plot(prices['Close'], color='black',linestyle='solid')
    # plt.title(outputTable)
    plt.tight_layout()
    plt.show()

t = yf.Ticker('SPY')
df = t.history(period='1d', interval='1m')

dates = []
prices = []
for rows in range(len(df)):
    time = df.index[rows].strftime('%H:%M:%S')
    # df.index[rows].rename(time, inplace=True)
    # print()
    # prices.append(df['Close'][rows])

print(df)
plotGraph(df)

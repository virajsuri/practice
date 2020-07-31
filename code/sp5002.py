import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
from datetime import datetime

sp500 = pdr.get_data_yahoo('^GSPC', start='1/1/1970', end= datetime.today())
print(sp500.head())
print("=====================================================================")
print(sp500.tail())

# plot hitorical closing price
sp500['Close'].plot(grid=True, figsize=(8, 5))
plt.show()

sp500['42d'] = np.round(pd.Series.rolling(sp500['Close'], window=42).mean(), 2)
sp500['252d'] = np.round(pd.Series.rolling(
    sp500['Close'], window=252).mean(), 2)

# Plot historical close, 42 day moving average and 252 day moving average 
sp500[['Close', '42d', '252d']].plot(grid=True, figsize=(8, 5))
plt.show()
print('\n===================================================================')
print('#data with SMAs incld')
print(sp500[['Close', '42d', '252d']].tail())
print("=====================================================================")
sp500['42-252'] = sp500['42d'] - sp500['252d']

print(sp500['42-252'].tail())

print("=====================================================================")

SD = 50
sp500['Regime'] = np.where(sp500['42-252'] > SD, 1, 0)
sp500['Regime'] = np.where(sp500['42-252'] < -SD, -1, sp500['Regime'])
print(sp500['Regime'].value_counts())
sp500['Regime'].plot(lw=1.25)
plt.ylim([-1.1, 1.1])
plt.show()

print("=====================================================================")
sp500['Market'] = np.log(sp500['Close'] / sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Regime'].shift(1) * sp500['Market']
sp500[['Market', 'Strategy']].cumsum().apply(
    np.exp).plot(grid=True, figsize=(8, 5))
plt.show()
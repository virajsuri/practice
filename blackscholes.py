import pybbg
import pandas as pd
import numpy as np
import scipy.stats as si
from sympy.stats import Normal, cdf

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

equity = ['MCD US Equity']
roundingData = pd.DataFrame([
                            ['IVOL_SIGMA','{0:.2%}',1,'Implied Volatility by Sigma'],
                            ['PX_LAST','${0:.2f}',1,'Last Price']
                            ])

spotPrice = 0
sigma = 0

def test_bdp(securities, roundingData):
        try:
            pipeline = pybbg.Pybbg()
            data = pd.DataFrame(pipeline.bdp(securities, roundingData[0]))
        except Exception as e: print(e)
        return(data) 

def euro_vanilla_call(S, K, T, r, sigma):
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call


def printFrame(table):
    strikeVals = []
    dateVals = []

    dollarsFromSpot = 50
    daysOfMaturity=100
     
    for index in table:
        sigma = table[index][0]/100
        spotPrice = table[index][1]

    #strikes
    for x in range(int(spotPrice-dollarsFromSpot), int(spotPrice+dollarsFromSpot)):
        strikeVals.append(x)
    
    #dates
    for x in range(daysOfMaturity):
        dateVals.append(x)


    payoffDF = pd.DataFrame(columns=dateVals, index=strikeVals)
    for column in range(len(payoffDF)):
        # print(column)
        for rows in range(len(dateVals)):
            price = euro_vanilla_call(spotPrice, payoffDF.index[column], rows, 0.0125, sigma)
            print(price)
            payoffDF.iloc[column][rows] = price
    
    print(payoffDF)

    x,y = np.meshgrid(payoffDF.columns.astype(float), payoffDF.index.astype(float))
    z = payoffDF.values
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
    ax.plot_wireframe(x,y,z)
    ax.set_ylabel("Strikes")
    ax.set_xlabel("Days to Maturity")
    ax.set_zlabel("Price of Option")

    fig.suptitle(str(equity[0])+" Options Price")
    fig.tight_layout()
    plt.show()

outputTable = test_bdp(equity, roundingData)
printFrame(outputTable)
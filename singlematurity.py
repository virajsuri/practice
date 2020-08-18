import pandas as pd
import numpy as np
import scipy.stats as si
from sympy.stats import Normal, cdf


callput = ""

def euro_vanilla(S, K, T, r, sigma, option = callput):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    if option == 'call':
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
    return result

def printFrame(daysToMat):
    strikeVals = []
    optionsPrice = []

    dollarsFromSpot = 50
    daysOfMaturity=100
     
    spotPrice = 210
    sigma = 2.7
    # for index in table:
    #     sigma = table[index][0]/100
    #     spotPrice = table[index][1]

    #strikes
    for x in range(int(spotPrice-dollarsFromSpot), int(spotPrice+dollarsFromSpot)):
        strikeVals.append(x)
    
    payoffDF = pd.DataFrame(columns=[daysToMat], index=strikeVals)
    # print(payoffDF)


    for column in range(len(payoffDF)):
        print(column)
        print(payoffDF[column])
        strikePrice = payoffDF.index[column]
        # for rows in range(daysToMat):
            # print(payoffDF.iloc[column][rows])

            # if(strikePrice>spotPrice):
            #     #call
            #     price = euro_vanilla(spotPrice, strikePrice, rows, 0.0125, sigma, "call")
            #     print(price)
            #     payoffDF.iloc[column][rows] = price
            # if(strikePrice<=spotPrice):
            #     #put
            #     price = euro_vanilla(spotPrice, strikePrice, rows, 0.0125, sigma, "put")
            #     print(price)
            #     payoffDF.iloc[column][rows] = price

    print(payoffDF)
    print(len(payoffDF.columns))


printFrame(30)
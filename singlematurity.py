import pandas as pd
import numpy as np
import scipy.stats as si
from sympy.stats import Normal, cdf
import matplotlib.pyplot as plt


def euro_vanilla(S, K, T, r, sigma, option):
    
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
    #single maturity, single strike price, different underlying prices

    underlyingVals = []
    dollarsFromSpot = 50
    spotPrice = 210
    sigma = 2.7

    #strikes
    for x in range(int(spotPrice-dollarsFromSpot), int(spotPrice+dollarsFromSpot)):
        underlyingVals.append(x)
    
    payoffDF = []

    for rows in range(len(underlyingVals)):
        print(rows)
        underlyingPrice = underlyingVals[rows]
        
        #if strike is greater than spot 
        if(240>underlyingPrice):
            payoffDF.append(0)
            continue
            
        else:
            #call
            price = euro_vanilla(underlyingPrice, 240, daysToMat, 0.0125, sigma, 'put')
            price = underlyingPrice-price
            print(str(spotPrice)+ " | "+str(underlyingPrice)+" | "+str(price)) 
            payoffDF.append(price)
        

    print(payoffDF)
    plotGraph(payoffDF)
 

def plotGraph(outputTable):
    print("Plotting graph")
    plt.figure(figsize=(10,4))
    plt.plot(outputTable, color='black',linestyle='solid')
    # plt.title(outputTable.columns[0])
    plt.tight_layout()
    plt.show()

printFrame(1)
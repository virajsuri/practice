import pybbg
import bdhPrintFrame
import showGraph
import datetime
import pandas as pd 
from dateutil.relativedelta import relativedelta

# security = ['58013MEH3 Corp']
security = ['MCD US Equity']


roundingDataEquities = pd.DataFrame([
                                    ['PX_LAST','${0:,.2f}',1,'Last Price'],
                                    ['CUR_MKT_CAP','${:,.0f}',1000,'Curr Mkt Cap'],
                                    ['PX_VOLUME','{0:,.0f}',1,'Volume'],
                                    ])

roundingDataBonds = pd.DataFrame([
                                 ['PX_LAST','${0:,.2f}',1,'Last Price'],
                                 ['BLP_SPRD_TO_BENCH_BID','{:,.1f}',1,'BBG Bid Sprd To Benchmark'], 
                                 ['BLP_SPRD_TO_BENCH_ASK','{:,.1f}',1,'BBG Ask Sprd To Benchmark'],   
                                 ])

def bdh(securities, roundingData, histDate, today):
    try:
        pipeline = pybbg.Pybbg()
        data = pd.DataFrame(pipeline.bdh(securities, roundingData, histDate, today))
        return(data)
    except Exception as e: print(e) 

today = datetime.datetime.today()
histDate = today + datetime.timedelta(days=-30)

outputTable = bdh(security, roundingDataEquities[0], histDate, today)
# print(outputTable)
bdhPrintFrame.printFrame(security, outputTable, roundingDataEquities)

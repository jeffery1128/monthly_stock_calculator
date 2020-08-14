# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:37:44 2020

@author: USER
"""

import pandas as pd
from yahoofinancials import YahooFinancials
import datetime as dt

def take_ticker_data(ticker,month,quantity):
    yahoo_financials = YahooFinancials(ticker)
    day = month *30
    end_date = (dt.date.today()).strftime('%Y-%m-%d')
    start_date = (dt.date.today()-dt.timedelta(day)).strftime('%Y-%m-%d')
    data = yahoo_financials.get_historical_price_data(start_date, end_date, "monthly")
    price = data[ticker]['prices']
    df =  pd.DataFrame(price)
    df.set_index('formatted_date', inplace = True)
    cost = df['close'].sum() * quantity
    #recent_price = df.loc[end_date]['close']
    print(cost)
    return 1
    


result= take_ticker_data("AAPL",12,2)  
print(result)

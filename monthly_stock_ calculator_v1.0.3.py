# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:37:44 2020

@author: USER
"""

import pandas as pd
from yahoofinancials import YahooFinancials
import datetime as dt
from firebase_admin import db
from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate("C:/Users/Chun Ho Tse/git/monthly_stock_calculator/monthly_stock_calculator/monthly-stock-calculator.json")
firebase_admin.initialize_app(cred,{ 
    'databaseURL': 'https://monthly-stock-calculator.firebaseio.com/'
})

def take_ticker_data(ticker,month,quantity):
    yahoo_financials = YahooFinancials(ticker)
    day = month *30
    end_date = (dt.date.today()).strftime('%Y-%m-%d')
    yesterday = (dt.date.today()-dt.timedelta(1)).strftime('%Y-%m-%d')
    start_date = (dt.date.today()-dt.timedelta(day)).strftime('%Y-%m-%d')
    month_data = yahoo_financials.get_historical_price_data(start_date, end_date, "monthly")
    daily_data = yahoo_financials.get_historical_price_data(start_date, end_date, "daily")
    df =  pd.DataFrame(month_data[ticker]['prices'])
    daily_df = pd.DataFrame(daily_data[ticker]['prices'])
    df.set_index('formatted_date', inplace = True)
    daily_df.set_index('formatted_date', inplace = True)
    cost = df['close'].sum() * quantity
    recent_price = df.loc[df.last_valid_index()]['close']
    total_quantity = month * quantity
    now_asset = recent_price * total_quantity
    average_price = cost / (total_quantity)
    percentage = ((now_asset - cost)/cost)*100
    print('Ticker : ',ticker)
    print('Cost : ',cost)
    print('Now Worth : ' , now_asset)
    print('Average Stock Price : ' , average_price)
    print('Recent Price : ' , recent_price)
    print('Win/Loss Percentage : ' , percentage ,'%')
    result= dict()
    result['Ticker'] = ticker
    result['month_duration'] = month
    result['Cost'] = round(cost,2)
    result['Now_Asset'] = round(now_asset,2)
    result['Average_stock_price'] = round(average_price,2)
    result['Recent_Price'] = round(recent_price,2)
    result['Percentage'] = round(percentage,2)
    return result
    
def firebase_callback(event):
    request = event.data
    ticker = request['ticker']
    month = request['month']
    quantity = request['quantity']
    result = take_ticker_data(ticker,month,quantity)
    ref = db.reference('/result')
    ref.set(result)
    print('Result has uploaded to firebase database!')

#result= take_ticker_data("NFLX",12,2)
#ref = db.reference('/')
#ref.set(result)

ref = db.reference('/request')
ref.listen(firebase_callback)

while 1 :
    pass
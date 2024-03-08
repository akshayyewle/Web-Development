from re import S
import streamlit as st
import os
import pandas as pd
import numpy as np
import yfinance as yf 
from datetime import date
import plotly.express as px 
import datetime as dt
from alpha_vantage.fundamentaldata import FundamentalData

# Set API Key
AV_Key = os.environ.get('Alpha_Vantage_API_Key')

# Page Header
st.title('Stock Dashboard')
st.write('Get Stock Data Analysis & Visualization')
Today_Date = date.today().strftime('%A %d %B %Y')
st.write(f'Today is {Today_Date}')

# Get Input Data
st.sidebar.subheader(body = f'Get Stock Data')
Ticker = st.sidebar.text_input(label='Enter Ticker Symbol', placeholder='TSLA', value='TSLA')
Start_Date = st.sidebar.date_input(label='Start Date',value = dt.date.today() - dt.timedelta(days=3*365))
End_Date = st.sidebar.date_input(label='End Date',value=dt.date.today())

# Get Basic Stock Info
st.subheader(body = f'Basic Info')
Stock_Data = yf.Ticker(Ticker)
Stock_Info = Stock_Data.get_info()
Stock_Name = Stock_Info['longName']
Stock_Country = Stock_Info['country']
Stock_Sector = Stock_Info['sector']
Stock_Industry = Stock_Info['industry']
Stock_Currency = Stock_Info['currency']
Stock_Description = Stock_Info['longBusinessSummary']

st.sidebar.subheader(body = f'Basic Info')
st.sidebar.write(f'Name: {Stock_Name}')
st.sidebar.write(f'Country: {Stock_Country}')
st.sidebar.write(f'Industry: {Stock_Industry}')
st.sidebar.write(f'Sector: {Stock_Sector}')
st.sidebar.write(f'Currency: {Stock_Description}')

# Get Stock Price Data
Stock_Price_Data = yf.download(tickers=Ticker, start=Start_Date, end=End_Date)
st.subheader(body = f'Last 10 Trading Session Data')
st.write('Currency: ', Stock_Currency)
st.dataframe(Stock_Price_Data.tail(7))

# Create Stock Price Plot
st.subheader(body = f'Stock Price of {Ticker}')
st.write('Currency: ', Stock_Currency)
st.selectbox('Select Chart Type', ['Line','Candlestick','Area'])
Stock_Price_Plot = px.area(Stock_Price_Data, x=Stock_Price_Data.index, y='Close')
st.plotly_chart(Stock_Price_Plot)

# Create Tabs
Pricing_Data, Fundamental_Data, News_Data, Management_Data = st.tabs(tabs=['Pricing Data','Fundamental Data', 
                                                                           'News Data','Management Data'])

with Pricing_Data:
    st.subheader('Pricing Movement')

    # Daily Price Change 
    Data02 = Stock_Price_Data
    Data02['Daily Change %'] = Data02['Close'] / Data02['Close'].shift(1) -1 
    Data02.dropna(inplace=True)
    # st.write(Data02)

    # Annual Returns
    Stock_Annual_Return = Data02['Close'].pct_change().mean() * 252 * 100
    Stock_Annual_Return = round(Stock_Annual_Return, 2)
    st.write('Annual Returns: ', Stock_Annual_Return,'%') 

    # Standard Deviation
    Stock_StdDev = Data02['Close'].pct_change().std() * np.sqrt(252) * 100
    Stock_StdDev = round(Stock_StdDev, 2)
    st.write('Standard Deviation: ', Stock_StdDev, '%')

    # Risk Adj Returns
    Stock_Risk_Adj_Returns = Stock_Annual_Return / Stock_StdDev
    Stock_Risk_Adj_Returns = round(Stock_Risk_Adj_Returns, 2)
    st.write('Risk Adj Returns: ',Stock_Risk_Adj_Returns ,'%')

    # Financial Ratios
    st.subheader('Financial Ratios')
    st.write('Short Ratio: ',Stock_Info['shortRatio'])
    st.write('Beta Ratio: ',Stock_Info['beta'])
    st.write('Trailing PE: ',Stock_Info['trailingPE'])
    st.write('Forward PE: ',Stock_Info['forwardPE'])
    # st.write('Earnings Growth: ',Stock_Info['earningsGrowth']*100)
    st.write('Market Capitalization: ',round(Stock_Data.basic_info['marketCap']/(10**9),2),'Billion USD')

with Fundamental_Data:
    st.header('Fundamental Data')
        
    # Balance Sheet
    st.subheader('Balance Sheet')
    Stock_Financial_Sheet = Stock_Data.get_financials()
    SFS = Stock_Financial_Sheet
    # SFS.columns = list(Stock_Financial_Sheet.T.iloc[0])
    st.write(SFS)
    
with News_Data:
    st.header('News Data')

with Management_Data:
    st.header('Management Data')

    for Officer in Stock_Info['companyOfficers']:
        st.subheader(Officer['title'])
        st.write('Name: ',Officer['name'])

        if 'age' not in Officer.keys():
            st.write('Age: ', 'Not Available')
        else:
            st.write('Age: ',Officer['age'])

        if 'totalPay' not in Officer.keys():
            st.write('Salary: ', 'Not Available')
        else:
            st.write('Salary: ', Officer['totalPay'], Stock_Currency, Officer['fiscalYear'])
        
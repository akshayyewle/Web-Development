import streamlit as st
import os
import pandas as pd
import numpy as np
import yfinance as yf 
from datetime import date
import plotly.express as px 
from alpha_vantage.fundamentaldata import FundamentalData

# Set API Key
AV_Key = os.environ.get('Alpha_Vantage_API_Key')

# Page Header
st.title('Stock Dashboard')
st.text('Get Stock Data Analysis & Visualization')

# Get Input Data
Ticker = st.sidebar.text_input(label='Enter Ticker Symbol', placeholder='TSLA')
Start_Date = st.sidebar.date_input(label='Start Date')
End_Date = st.sidebar.date_input(label='End Date')

# Get Stock Price Data
Stock_Price_Data = yf.download(tickers=Ticker, start=Start_Date, end=End_Date)
st.dataframe(Stock_Price_Data.tail(7))

# Create Stock Price Plot
Stock_Price_Plot = px.area(Stock_Price_Data, x=Stock_Price_Data.index, y='Close', title=f'Stock Price of {Ticker}')
st.plotly_chart(Stock_Price_Plot)

# Create Tabs
Pricing_Data, Fundamental_Data, News_Data = st.tabs(tabs=['Pricing Data', 'Fundamental Data', 'News Data'])

with Pricing_Data:
    st.header('Pricing Movement')

    # Daily Price Change 
    Data02 = Stock_Price_Data
    Data02['Daily Change %'] = Data02['Close'] / Data02['Close'].shift(1) -1 
    Data02.dropna(inplace=True)
    st.write(Data02)

    # Annual Returns
    Stock_Annual_Return = Data02['Close'].pct_change().mean() * 252 * 100
    Stock_Annual_Return = round(Stock_Annual_Return, 2)
    st.write(f'Annual Returns Are {Stock_Annual_Return} %') 

    # Standard Deviation
    Stock_StdDev = Data02['Close'].pct_change().std() * np.sqrt(252) * 100
    Stock_StdDev = round(Stock_StdDev, 2)
    st.write(f'Standard Deviation Is {Stock_StdDev} %')

    # Risk Adj Returns
    Stock_Risk_Adj_Returns = Stock_Annual_Return / Stock_StdDev
    Stock_Risk_Adj_Returns = round(Stock_Risk_Adj_Returns, 2)
    st.write(f'Risk Adj Returns Are {Stock_Risk_Adj_Returns} %')

with Fundamental_Data:
    st.header('Fundamental Data')
    
    # Get Fundamental Data
    Stock_Fundamental_Data = FundamentalData(key=AV_Key, output_format='pandas')
    
    # Balance Sheet
    st.subheader('Balance Sheet')
    Stock_Balance_Sheet = Stock_Fundamental_Data.get_balance_sheet_annual(symbol=Ticker)
    st.write(Stock_Balance_Sheet)
with News_Data:
    st.header('News Data')
    
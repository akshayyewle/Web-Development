import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf 
from datetime import date
import plotly.express as px 

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
    st.header('Pricing Data')
    st.dataframe(Stock_Price_Data.tail(7))

with Fundamental_Data:
    st.header('Fundamental Data')
    st.dataframe(Stock_Price_Data.tail(7))
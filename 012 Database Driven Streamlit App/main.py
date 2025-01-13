import streamlit as st
import sqlite3
import pandas as pd
import datetime as dt 

# Create a connection object
DATABASE_NAME = "expenses.db"
DEFAULT_CATEGORIES = ["Rent", "Utilities", "Groceries"]
cat_list = ""
for i in DEFAULT_CATEGORIES:
    cat_list = cat_list + "(\"" + i + "\"),"


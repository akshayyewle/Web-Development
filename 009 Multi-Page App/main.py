import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection

st.title('Hello, Streamlit!')

# Connect to local Postgres Database
conn = FilesConnection()
conn.connect()


p1 = st.Page('Page 1')
p2 = st.Page('Page 2')
p3 = st.Page('Page 3')

pg = st.Navigation(p1, p2, p3)
pg.run()
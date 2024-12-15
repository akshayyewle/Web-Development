import streamlit as st

st.title('Hello, Streamlit!')

p1 = st.Page('Page 1')
p2 = st.Page('Page 2')
p3 = st.Page('Page 3')

pg = st.Navigation(p1, p2, p3)
pg.run()
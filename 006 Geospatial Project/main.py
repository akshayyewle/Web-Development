import streamlit as st
import folium
st.set_page_config(layout='wide', page_title='Geospatial Analysis')

st.title('Geospatial Analysis')
st.write('This is a geospatial analysis app')

col01, col02 = st.columns([0.3,0.6],gap='small')
with col01:
    st.subheader('Enter a location')
    location = st.text_input('Location', value='New York City')
    lat = st.number_input('Latitude', value=40.7128, step=0.0001, format='%f')
    long = st.number_input('Longitude', value=-74.0060, step=0.0001, format='%f')
    st.write('Latitude:', lat, 'Longitude:', long)

with col02:
    col02.map(latitude=lat, longitude=long,zoom=15,use_container_width=False)
# Import Dependencies 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from st_files_connection import FilesConnection
# from pystac_client import Client
# from odc.stac import load
import hmac

# Import Custom Functions
from functions import search_satellite_images, get_bbox_with_buffer,count_classified_pixels     

# App Title
st.title("Satellite Image Viewer")

# Default Parameters
collections=["sentinel-2-l2a"]
columns = ['collection', 'start_date', 'end_date','min_cloud_cover', 'max_cloud_cover', 
           'longitude', 'latitude','buffer']
def_location_coord = (51.5074,0.1278) # London, UK
default_zoom = 10

df = pd.DataFrame(columns=columns)

# Initialize session state for date_labels and user_date
if 'date_labels' not in st.session_state:
    st.session_state.date_labels = []

if 'data' not in st.session_state:
    st.session_state.data = None

if 'user_date' not in st.session_state:
    st.session_state.user_date = None

if 'user_date_index' not in st.session_state:
    st.session_state.user_date_index = 0

if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(columns=df.columns)

# User input form
with st.form(key='my_form'):
    collection = st.selectbox('Select Collection *', collections)
    start_date = st.date_input('Start Date *',)
    end_date = st.date_input('End Date *')
    max_cloud_cover = st.slider('Max Cloud Cover *', 0, 100, step=5,value=5)
    latitude = st.number_input('Latitude *',format="%.4f",value=def_location_coord[0],step=0.0001)
    longitude = st.number_input('Longitude *',format="%.4f",value=def_location_coord[1],step=0.0001)
    buffer = st.number_input('Buffer (0.01 = 1Km) *',format="%.2f",value=10)

    # User instructions
    st.markdown('*Required')

    # Submit button
    submit_button_run = st.form_submit_button(label="Run",type="primary")
    submit_button_list = st.form_submit_button(label="List Available Images",type="primary")
    submit_button_viz = st.form_submit_button(label="Visualize", type="primary")

# If the user clicks the "Run" button    
if submit_button_run:
        new_df=pd.DataFrame(
            [
                {   
                    "collection": collection,
                    "start_date":start_date.strftime("%Y-%m-%d"),
                    "end_date": end_date.strftime("%Y-%m-%d"),
                    "max_cloud_cover":max_cloud_cover,
                    "longitude": longitude,
                    "latitude": latitude,
                    "buffer": buffer,

                }

            ]
        )

        st.session_state.mdf = pd.concat([st.session_state.mdf, new_df], axis=0)
        st.dataframe(st.session_state.mdf)
        st.success("Your request successfully submitted!")

        data = search_satellite_images(collection=collection,
                                       date=f"{start_date}/{end_date}",
                                       cloud_cover=(0, max_cloud_cover),
                                       bbox=get_bbox_with_buffer(latitude=latitude, longitude=longitude, buffer=buffer))
        st.session_state.data = data

        date_labels = []
        # Determine the number of time steps
        numb_days = len(data.time)
        # Iterate through each time step
        for t in range(numb_days):
            scl_image = data[["scl"]].isel(time=t).to_array()
            dt = pd.to_datetime(scl_image.time.values)
            year = dt.year
            month = dt.month
            day = dt.day
            date_string = f"{year}-{month:02d}-{day:02d}"
            date_labels.append(date_string)

        st.session_state.date_labels= date_labels

# If the user clicks the "List Available Images" button
if submit_button_list:
        user_date=st.selectbox("Available Images*",options=st.session_state.date_labels,index=None)
        if user_date:
            st.session_state.user_date = user_date
            st.session_state.user_date_index = user_date.index()

if submit_button_viz:

        date_string_title= f"Sentinel-2 Image over AOI"
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))  

        rgb = st.session_state.data[["red", "green", "blue"]].isel(time=st.session_state.user_date_index).to_array()
        rgb.plot.imshow(robust=True, ax=axs[0])
        axs[0].axis('off')  # Hide the axes ticks and labels
        axs[0].set_title(date_string_title)

        # Preparing data 
        counts = count_classified_pixels(st.session_state.data, st.session_state.user_date_index )
        labels = list(counts.keys())
        values = list(counts.values())
        colors = ['DarkGrey', 'chartreuse', 'DarkOrange', 'cyan']
        explode = (0.3, 0.1, 0.1, 0.1)  # Exploding the first slice

        # Plotting the pie chart 
        axs[1].pie(values, labels=labels, colors=colors, autopct='%1.0f%%', startangle=140, explode=explode)
        axs[1].legend(labels, loc='best', bbox_to_anchor=(1, 0.5))
        axs[1].axis('equal')  # Ensure the pie chart is a circle
        axs[1].set_title('Distribution of Classes')

        # Display the figure in Streamlit
        st.pyplot(fig)
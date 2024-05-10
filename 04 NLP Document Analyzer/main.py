!pip install streamlit
!pip install pandas
!pip install nltk

import os
import streamlit as st
import pandas as pd
from nltk.corpus import stopwords


# Page Margins
st.set_page_config(layout="wide",page_title="NLP Document Analyser",page_icon="Images/a0e339a68d74573066ac96f28c0f3600.jpg")
margins_css = """
    <style>
        .main > div {
            padding-left: 3rem;
            padding-right: 3rem;
            padding-top: 0.25rem
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

st.sidebar.image("https://images.unsplash.com/photo-1541854615901-93c354197834?q=80&w=2073&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",width=250)
st.sidebar.header("NLP Document Analyser")


st.header("NLP Document Analyser")
st.subheader("Enter your text or document")

# Input Document
input_file = st.file_uploader("**Upload your document**",help='Upload your document',
                            accept_multiple_files=False,type=['txt'])

# Input Similarity Score
similarity_req = st.slider('**Required Contextual Similarity**',min_value=float(0),max_value=float(1),step=0.01,value=0.5,
                           help='How similar the words should be?')

# Input Keywords
input_keywords_string = st.text_input("**Enter Search keywords**",help='What Words would you like to look for?')
input_keywords_list = input_keywords_string.lower().split(',')
input_keywords_list = [word.strip() for word in input_keywords_list]
st.text(input_keywords_list)

# Omission Keywords
omit_keywords_string = st.text_input("**Enter Omission Keywords**",help='What Words would you like to omit?')
omit_keywords_list = omit_keywords_string.lower().split(',')
omit_keywords_list = [word.strip() for word in omit_keywords_list]
st.text(omit_keywords_list)

# Read Document Text
st.subheader("Reading Document...")
if input_file:
    # st.text('File Name: ',input_file.name)
    # st.text('File Type: ',input_file.type)
    input_text = input_file.read().decode("utf-8")
    input_word_list = input_text.lower().split()
    input_word_list = [word.strip() for word in input_word_list]
    input_word_list = [word for word in input_word_list if word not in stopwords.words('english')]
    input_word_list = [word for word in input_word_list if len(word)>2]
    st.text(input_word_list)

# Text Output
st.sidebar.header("Output")
st.subheader("Output")
# word_count = input_word_list.
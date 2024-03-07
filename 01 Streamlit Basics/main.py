import streamlit as st

# Display Text Data
st.title('My first app')
st.subheader('My first subtitle')
st.write('Hello World')
st.video(data='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
st.image('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')

# Create Input Options
st.header('Input Options')
st.text_input('Enter your name',placeholder='John')
st.number_input('Enter your age',min_value=18,max_value=100,placeholder=18)
st.button('Click me')
st.checkbox('Tick me')
st.radio('Pick me',('One','Two','Three'))
st.toggle('Warp Mode',True)
st.selectbox('Select me',('One','Two','Three'))
st.multiselect('Pick me',options=('One','Two','Three'))
st.slider('Slide me',min_value=0,max_value=100,step=5)
st.select_slider('Slide to select',options=('One','Two','Three'))

st.file_uploader('Upload a file',type=['jpg','png','pdf'])
# st.page_link('Google',url='https://www.google.com')
st.link_button('Google',url='https://www.google.com')
st.date_input('Enter a date')
st.time_input('Enter a time')
st.camera_input('Take A Picture')
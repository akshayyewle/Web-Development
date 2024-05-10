import streamlit as st
st.set_page_config(layout="wide")

# Title
col1, col2 = st.columns([1,0.2])
with col1:
    st.title('ABC Facility Management System')
with col2:
    st.image('Images/a0e339a68d74573066ac96f28c0f3600.jpg',width=100)

# Navigation Bar
st.header('Navigation Bar')

# Sign In Page
col3, col4 = st.columns([1,0.5])
with col3:
    # Backgroun Image
    background_image_url = "Images/sean-pollock-PhYq704ffdA-unsplash.jpg"
    st.image(background_image_url, use_column_width=True)
with col4:
    # Sign In Box
    st.header('Sign In')
    st.text_input('Enter You Username',placeholder='Username')
    st.text_input('Enter Your Password',placeholder='Password')
    st.checkbox('Remember Me')
    st.button('Sign In')

# About Section
st.subheader('About Us')
st.markdown(
    '''Welcome to **TechFacility Solutions**, your premier partner in integrating cutting-edge technology with seamless facility management. Our mission is to revolutionize the way businesses operate by providing smart, secure, and efficient management services. With a focus on innovation, we offer a comprehensive suite of services including **facility management**, **advanced access control**, and **intelligent parking management**.
At TechFacility Solutions, we understand that the backbone of any successful enterprise is the smooth functioning of its facilities. That's why we harness the power of technology to ensure your operations run like clockwork. Our **state-of-the-art access control systems** guarantee security and convenience, while our **smart parking solutions** optimize space usage and improve user experience.
Join us in embracing the future of business operations, where technology drives efficiency and management is synonymous with excellence. **TechFacility Solutions** is not just a service provider; we are your strategic ally in building a smarter, safer, and more sustainable business environment. 🌟'''
)

# Page Footer
st.subheader('Social Media')
# st.markdown("---")
import streamlit as st

st.title("Welcome to the Demo App")

# Create signin page with 2 tabs for login and signup
tab1, tab2 = st.tabs(["Login", "Signup"])

with tab1:
    st.subheader("Login Section")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.button("Login")

    # Check Password
    if submit:
        # Check if username and password match
        if username in st.secrets["passwords"] and password == st.secrets["passwords"][username]:
            st.write("Login Successful")
        else:
            st.write("Invalid Username or Password")

with tab2:
    st.subheader("Signup Section")
    new_username = st.text_input("Create Username",)
    new_password = st.text_input("Create Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if new_password != confirm_password:
        st.write("Passwords do not match")
    signup = st.button("Signup")
    if signup:
        # Add credentials to a secret.toml file
        with open(".streamlit/secrets.toml", "a") as f:
            f.write(f"[passwords] {new_username} = '{new_password}")
        st.write("Signup Successful")
    else:
        st.write("Signup Failed")
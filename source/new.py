import streamlit as st
import os


# Initialize uploaded file variable
uploaded_file = None


# New Web button callback
def on_new_web_button_click():
    global uploaded_file
    if uploaded_file is not None:
        # Remove the uploaded file from the system
        os.remove(uploaded_file.name)
        uploaded_file = None
        st.empty()
    uploaded_file = None
    st.empty()
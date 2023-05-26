import streamlit as st
from PIL import Image

from source.prediction import prediction_output


def home():
    # Add image
    image = Image.open("assets/images/logo.png")
    st.image(image, use_column_width=True)

    # Input file upload section
    uploaded_file = st.file_uploader("Upload your input file (.txt)", type=['txt'])
    st.markdown("[Example input file](https://raw.githubusercontent.com/getdaniel/bc-drug/main/ML/aromatase_exp.txt)")

    # Display a message if no file is uploaded
    if uploaded_file is None:
        st.info("No file uploaded or file is empty. Please upload a file.")

    # Prediction section
    if st.button("Predict", use_container_width=True) and uploaded_file is not None:
        prediction_output(uploaded_file)
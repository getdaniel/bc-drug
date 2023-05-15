import streamlit as st
import subprocess
import base64
import os
import pickle
import pandas as pd
from PIL import Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

# Initialize Firebase app
cred = credentials.Certificate("js/drug-discovery-d551f-firebase-adminsdk-dari3-50acf314ae.json")
try:
    # Try to get the app instance if it has already been initialized
    firebase_admin.get_app()
except ValueError:
    # Initialize the app if it has not been initialized yet
    firebase_admin.initialize_app(cred, name='streamlit-app', options={
        'databaseURL': 'https://drug-discovery-d551f-default-rtdb.firebaseio.com'
    })


# Molecular descriptor calculator
def desc_calc():
    # Performs the descriptor calculation
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./ML/PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./ML/PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file ML/descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('ML/molecule.smi')

# File download
def filedownload(df):
    csv = df.to_csv(index=False)
    # strings <-> bytes conversions
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

# Model building
def build_model(input_data):
    # Reads in saved regression model
    load_model = pickle.load(open('ML/aromatase.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(load_data[1], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)

# Define feedback modal function
def feedback_modal():
    # Create modal overlay
    feedback_modal = st.beta_expander("Send Feedback")
    with feedback_modal:
        st.write("Please enter your email and feedback message below:")

        # Email input
        email = st.text_input("Email:", key="feedback_email")

        # Feedback message input
        message = st.text_area("Feedback message:", key="feedback_message")

        # "Send Feedback" button
        if st.button("Send Feedback"):
            # Check if all fields are filled out
            if not email or not message:
                st.warning("Please enter your email and feedback message.")
            else:
                # Save feedback to Firebase Realtime Database
                ref = db.reference('feedback')
                ref.push({
                    'email': email,
                    'message': message,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                st.success("Thank you for your feedback!")
                email = ""
                message = ""

# Set page title and icon
st.set_page_config(page_title="Drug Discovery",
                   page_icon="assets/images/bio_logo.png")

# Set title to be centered
st.markdown("<h2 style='text-align: center;'>Drug Discovery Using AI for Breast Cancer</h2>",
            unsafe_allow_html=True)

# Add image
image = Image.open("assets/images/logo.png")
st.image(image, use_column_width=True)

# Side bar
st.markdown(
    """
   <style>
        [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 200px;
           max-width: 200px;
       }
    """,
    unsafe_allow_html=True,
)

# Add buttons to sidebar
st.sidebar.button("New Web", use_container_width=True)
st.sidebar.button("Settings", use_container_width=True)

# Feedback button
if st.sidebar.button("Feedback", use_container_width=True):
    # Open feedback modal form
    st.sidebar.markdown("---")
    feedback_modal()

st.sidebar.button("History", use_container_width=True)
st.sidebar.button("Log Out", use_container_width=True)

# Input file upload section
uploaded_file = st.file_uploader("Upload your input file (.txt)", type=['txt'])
st.markdown("[Example input file](https://raw.githubusercontent.com/getdaniel/bc-drug/main/ML/aromatase_exp.txt)")

# Display a message if no file is uploaded
if uploaded_file is None:
    st.info("No file uploaded or file is empty. Please upload a file.")

# Prediction section
if st.button("Predict", use_container_width=True) and uploaded_file is not None:
    # Read input file
    load_data = pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('ML/molecule.smi', sep='\t', header=False, index=False)

    # Display original input data
    st.header('**Input Data with Dataframe**')
    st.write(load_data)

    # Calculate descriptors
    with st.spinner("Calculating Descriptors..."):
        desc_calc()

    # Display calculated descriptors
    st.header('**Calculated Molecular Descriptors**')
    desc = pd.read_csv('ML/descriptors_output.csv')
    st.write(desc)
    st.write(desc.shape)

    # Read descriptor list used in previously built model
    st.header('**Subset of Descriptors from the Models**')
    Xlist = list(pd.read_csv('ML/descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # Apply trained model to make prediction
    Xlist = list(pd.read_csv('ML/descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    build_model(desc_subset)
import streamlit as st
import subprocess
import base64
import os
import pickle
import pandas as pd
from PIL import Image

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

def styled_sidebar_button(label):
    """
    A decorator function that adds some styling to a Streamlit sidebar button.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Set the button style
            button_style = 'background-color: transparent; color: white; border: none; border-bottom: 2px solid transparent; padding: 0.5rem 1rem; font-weight: bold;'

            # Add the button to the Streamlit sidebar
            button_clicked = st.sidebar.button(label, key=label, help=func.__doc__, style=button_style)

            # Call the function if the button is clicked
            if button_clicked:
                func(*args, **kwargs)

        return wrapper

    return decorator

# Define the styled buttons using the decorator
@styled_sidebar_button("New Web")
def new_web():
    st.write("New Web clicked!")

@styled_sidebar_button("Settings")
def settings():
    st.write("Settings clicked!")

@styled_sidebar_button("Feedbacks")
def feedbacks():
    st.write("Feedbacks clicked!")

@styled_sidebar_button("History")
def history():
    st.write("History clicked!")

@styled_sidebar_button("Log Out")
def log_out():
    st.write("Log Out clicked!")

# Set the CSS style for the sidebar buttons
st.markdown("""
    <style>
        .sidebar .css-1vwm2ni:hover {
            background-color: #f5f5f5;
            border-bottom: 2px solid #f5f5f5;
        }

        .sidebar .css-1vwm2ni {
            width: 100%;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# Input file here
uploaded_file = st.file_uploader("Upload your input file", type=['txt'])
st.markdown("""
[Example input file](https://raw.githubusercontent.com/getdaniel/bc-drug/main/ML/aromatase_exp.txt)
""")


if st.button('Predict'):
    load_data = pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('ML/molecule.smi', sep='\t', header=False, index=False)

    st.header('**Original input data**')
    st.write(load_data)

    with st.spinner("Calculating descriptors..."):
        desc_calc()

    # Read in calculated descriptors and display the dataframe
    st.header('**Calculated molecular descriptors**')
    desc = pd.read_csv('ML/descriptors_output.csv')
    st.write(desc)
    st.write(desc.shape)

    # Read descriptor list used in previously built model
    st.header('**Subset of descriptors from previously built models**')
    Xlist = list(pd.read_csv('ML/descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # Apply trained model to make prediction on query compounds
    build_model(desc_subset)
else:
    st.info('Upload input data in the above button to start!')

import streamlit as st
from PIL import Image
from streamlit_modal import Modal
import pandas as pd

from source.descriptors import desc_calc
from source.model import build_model
from source.feedback import handle_user_feedback


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

modal = Modal("Feedback", key="feedback_button")
# Feedback button in the sidebar
if st.sidebar.button("Feedback", use_container_width=True):
    modal.open()

handle_user_feedback(modal)

st.sidebar.button("History", use_container_width=True)
st.sidebar.button("Log Out", use_container_width=True)

# Input file upload section
uploaded_file = st.file_uploader("Upload your input file (.txt)", type=['txt'])
st.markdown(
    "[Example input file](https://raw.githubusercontent.com/getdaniel/bc-drug/main/ML/aromatase_exp.txt)")

# Display a message if no file is uploaded
if uploaded_file is None:
    st.info("No file uploaded or file is empty. Please upload a file.")

# Prediction section
if st.button("Predict", use_container_width=True) and uploaded_file is not None:
    # Read input file
    load_data = pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('molecule.smi', sep='\t', header=False, index=False)

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
    build_model(load_data, desc_subset)
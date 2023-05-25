import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from streamlit_modal import Modal
from stmol import *

from source.feedback import handle_user_feedback
from source.logout import handle_logout
from source.history import handle_history
from source.settings import handle_settings
from source.prediction import prediction_output
from source.new import on_new_web_button_click


# Set page title and icon
st.set_page_config(page_title="Drug Discovery",
                   page_icon="assets/images/bio_logo.png")

# Hide custom made with streamlit
# MainMenu {visibility: hidden;}
hide_made_with = """
                <style>
                    footer {visibility: hidden;}
                </style>
                 """
st.markdown(hide_made_with, unsafe_allow_html=True)

# Set title to be centered
st.markdown("<h2 style='text-align: center;'>Drug Discovery Using AI for Breast Cancer</h2>",
            unsafe_allow_html=True)

# Add image
image = Image.open("assets/images/logo.png")
st.image(image, use_column_width=True)

# The render_pdb() function accepts any PDB ID and returns a py3Dmol object.
showmol(render_pdb(id='3EQM'))

st.title("3D Mol Visualization")

id = st.text_input("Enter your protein ID")

components.html("""
                <script src="https://3Dmol.org/build/3Dmol-min.js"></script>     
                <script src="https://3Dmol.org/build/3Dmol.ui-min.js"></script>  
                <div style="height: 400px; width: 400px; position: relative;" class='viewer_3Dmoljs' data-pdb={} data-backgroundcolor='0xffffff' data-ui='true' data-style1='cartoon:color=spectrum' data-spin='axis:y;speed:1'></div>
                """.format(id), width=700, height=500
            )

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
if st.sidebar.button("New", use_container_width=True):
    on_new_web_button_click()

setting_modal = Modal("Settings", key="settings_button")
if st.sidebar.button("Settings", use_container_width=True):
    setting_modal.open()

handle_settings(setting_modal)

feedback_modal = Modal("Feedback", key="feedback_button")
if st.sidebar.button("Feedback", use_container_width=True):
    feedback_modal.open()

handle_user_feedback(feedback_modal)

history_modal = Modal("History", key="history_button")
if st.sidebar.button("History", use_container_width=True):
    history_modal.open()

handle_history(history_modal)

logout_modal = Modal("Logout", key="logout_button")
if st.sidebar.button("Log Out", use_container_width=True):
    logout_modal.open()

handle_logout(logout_modal)

# Input file upload section
uploaded_file = st.file_uploader("Upload your input file (.txt)", type=['txt'])
st.markdown(
    "[Example input file](https://raw.githubusercontent.com/getdaniel/bc-drug/main/ML/aromatase_exp.txt)")

# Display a message if no file is uploaded
if uploaded_file is None:
    st.info("No file uploaded or file is empty. Please upload a file.")

# Prediction section
if st.button("Predict", use_container_width=True) and uploaded_file is not None:
    prediction_output(uploaded_file)
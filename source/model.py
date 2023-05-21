import pickle
import pandas as pd
import streamlit as st

from source.file_download import filedownload

# Model building
def build_model(load_data, input_data):
    if input_data.shape[0] == 0:
        st.info("Input data has zero samples/ No descriptor Value. Please provide valid input data.")
    else:
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

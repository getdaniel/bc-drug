import pickle
import pandas as pd
import streamlit as st

from source.file_download import filedownload

# Define color codes
green_color = '#00FF00'
yellow_color = '#FFFF00'
red_color = '#FF0000'

# Model building
def build_model(load_data, input_data):
    if input_data.shape[0] == 0:
        st.info(
            "Input data has zero samples/ No descriptor Value. Please provide valid input data.")
    else:
        # Reads in saved regression model
        load_model = pickle.load(open('ML/aromatase.pkl', 'rb'))

        # Apply model to make predictions
        prediction = load_model.predict(input_data)
        st.header('**Prediction Output**')
        molecule_name = pd.Series(load_data[1], name='molecule_name')
        prediction_output = pd.Series(prediction, name='pIC50')
        df = pd.concat([molecule_name, prediction_output], axis=1)
        st.write(df)

        # Draw a bar chart with molecule_name as X-axis and prediction_output as Y-axis
        st.header('**Graphical Prediction Output**')
        chart_data = df.set_index('molecule_name')

        # Create a new column for bar color based on pIC50 values
        chart_data['color'] = chart_data['pIC50'].apply(
            lambda x: green_color if x >= 6.5 else (yellow_color if 4.5 <= x < 6.5 else red_color))

        # Plot the bar chart with color-coded bars
        st.bar_chart(chart_data['pIC50'], color=chart_data['color'])

        # download the predicted csv file
        st.markdown(filedownload(df), unsafe_allow_html=True)
import pickle
import pandas as pd
import streamlit as st
import plotly.express as px
from rdkit import Chem
from rdkit.Chem import Draw

from source.file_download import filedownload

# Define color codes
green_color = '#00FF00'
yellow_color = '#FFFF00'
red_color = '#FF0000'

# Model building
def build_model(load_data, input_data):
    if input_data.shape[0] == 0:
        st.info("Input data has zero samples/ No descriptor Value. Please provide valid input data.")
    else:
        # Reads in saved regression model
        load_model = pickle.load(open('ML/aromatase.pkl', 'rb'))

        # Apply model to make predictions
        prediction = load_model.predict(input_data)
        st.header('**Prediction Output**')

        # Create a dataframe with molecule_name, pIC50 and SMILES
        molecule_name = pd.Series(load_data[1], name='molecule_name')
        smiles = pd.Series(load_data[0], name='smiles')
        prediction_output = pd.Series(prediction, name='pIC50')
        df = pd.concat([molecule_name, smiles, prediction_output], axis=1)

        # Apply conditional formatting to the pIC50 column
        def color_map(val):
            if val >= 6.5:
                color = 'background-color: green'
            elif 4.0 <= val < 6.5:
                color = 'background-color: yellow'
            else:
                color = 'background-color: red'
            return color

        # Apply the color_map function to the pIC50 column and display the dataframe
        st.dataframe(df.style.applymap(color_map, subset=['pIC50']), height=400)

        # Display the dataframe
        # st.write(df)

        # Display the 3D structure for each chemical
        for index, row in df.iterrows():
            st.markdown(f"#### Chemical: {row['molecule_name']}")

            # Replace with your own implementation to load the 3D structure
            mol = Chem.MolFromSmiles(row['smiles'])

            # Generate the 3D structure image using RDKit
            image = Draw.MolToImage(mol, size=(700, 250))

            # Display the image using Streamlit
            st.image(image)

        # Draw a bar chart with molecule_name as X-axis and prediction_output as Y-axis
        st.header('**Graphical Prediction Output**')
        chart_data = df.set_index('molecule_name')

        # Create a bar chart using plotly express with default colors
        fig = px.bar(chart_data, x=chart_data.index, y='pIC50')

        # Customize the chart appearance
        fig.update_layout(showlegend=False)  # Hide the color legend

        # Render the chart in Streamlit
        st.plotly_chart(fig)


        # download the predicted csv file
        st.markdown(filedownload(df), unsafe_allow_html=True)
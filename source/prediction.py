import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw

from source.model import build_model
from source.descriptors import desc_calc


def prediction_output(uploaded_file):
    # Read input file
    load_data = pd.read_table(uploaded_file, sep=' ', header=None)
    load_data.to_csv('molecule.smi', sep='\t', header=False, index=False)

    # Display original input data
    st.markdown(
                "<h4 style='text-align: center;'>Input Data with Data Frame</h4>",
                unsafe_allow_html=True
                )
    st.write(load_data)

    # Display 2D structure images
    st.markdown(
                "<h4 style='text-align: center;'>2D Strucure of the Molecule</h4>",
                unsafe_allow_html=True
                )
    for index, row in load_data.iterrows():
        st.markdown(f"##### Chemical: {row[1]}")

        mol = Chem.MolFromSmiles(row[0])
        if mol is not None:
            image = Draw.MolToImage(mol, size=(700, 250))
            st.image(image)
        else:
            st.write("Invalid SMILES string")

    # Calculate descriptors
    with st.spinner("Calculating Descriptors..."):
        desc_calc()

    # Display calculated descriptors
    # st.markdown(
    #             "<h4 style='text-align: center;'>Calculated Molecular Descriptors</h4>",
    #             unsafe_allow_html=True
    #             )
    desc = pd.read_csv('ML/descriptors_output.csv')
    # st.write(desc)
    # st.write(desc.shape)

    # Read descriptor list used in previously built model
    st.markdown(
                "<h4 style='text-align: center;'>Subset of Descriptors from the Models</h4>",
                unsafe_allow_html=True
                )
    Xlist = list(pd.read_csv('ML/descriptor_list.csv').columns)
    desc_subset = desc[Xlist]
    st.write(desc_subset)
    st.write(desc_subset.shape)

    # Apply trained model to make prediction
    build_model(load_data, desc_subset)
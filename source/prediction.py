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
    st.header('**Input Data with Data Frame**')
    st.write(load_data)

    # Display 2D structure images
    st.header('**2D Structure Images**')
    for index, row in load_data.iterrows():
        st.markdown(f"#### Chemical: {row[1]}")

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
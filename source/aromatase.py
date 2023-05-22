import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
import streamlit.components.v1 as components


def aromatase_structure():
    # Define the URL of the animated 3D view
    view_url = 'https://www.rcsb.org/3d-view/3EQM'

    # Display the animated 3D view using Streamlit components
    st.header('Aromatase Enzyme 3D Structure')
    components.iframe(view_url, height=800)
    
    # Define the SMILES notation for aromatase
    smiles = "CC1=CC(=CC=C1CCC(=O)NC2=CC=C(C=C2)Cl)O"

    # Convert SMILES to RDKit molecule object
    mol = Chem.MolFromSmiles(smiles)

    # Generate the 3D structure image using RDKit
    image = Draw.MolToImage(mol, size=(400, 100))

    # Display the image using Streamlit
    st.image(image, use_column_width=True)
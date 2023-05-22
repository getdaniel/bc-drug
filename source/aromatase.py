import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

def aromatase_structure():
    # Define the SMILES notation for aromatase
    smiles = "CC1=CC(=CC=C1CCC(=O)NC2=CC=C(C=C2)Cl)O"

    # Convert SMILES to RDKit molecule object
    mol = Chem.MolFromSmiles(smiles)

    # Generate the 3D structure image using RDKit
    image = Draw.MolToImage(mol, size=(400, 200))

    # Display the image using Streamlit
    st.image(image, use_column_width=True)
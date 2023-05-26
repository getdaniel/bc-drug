import streamlit as st
import streamlit.components.v1 as components

def show_3d_visualization():
    st.title("3D Mol Visualization")
    
    id = st.text_input("Enter your protein ID", value="3EQM", help="Example: 3EQM")
    
    components.html("""
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>     
        <script src="https://3Dmol.org/build/3Dmol.ui-min.js"></script>  
        <div style="height: 400px; width: 600px; position: relative;" class='viewer_3Dmoljs' data-pdb={} data-backgroundcolor='0xffffff' data-style='stick' data-style1='cartoon:color=spectrum' data-spin='axis:y;speed:1' data-ui='true'></div>
    """.format(id), width=500, height=500)
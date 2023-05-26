import streamlit as st
import streamlit.components.v1 as components

def show_3d_visualization():
    # Set title to be centered
    st.markdown(
                "<h2 style='text-align: center;'>3D Molecular View</h2>",
                unsafe_allow_html=True
                )
    
    id = st.text_input(
                    "Enter your protein ID",
                    value="3EQM",
                    help="Example: 3EQM or Vist [RSCB Website](https://www.rcsb.org) for more"
                )
    
    # Define the CSS styles for the viewer container
    viewer_styles = """
    .viewer-container {
        width: 100%;
        height: 0;
        padding-bottom: 75%; /* Adjust the aspect ratio based on your needs */
        position: relative;
    }

    .viewer_3Dmoljs {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }
    """

    # Add the CSS styles to the page
    st.markdown(f"<style>{viewer_styles}</style>", unsafe_allow_html=True)

    # Generate the HTML code for the viewer
    html_code = """
    <div class='viewer-container'>
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <script src="https://3Dmol.org/build/3Dmol.ui-min.js"></script>
        <div class='viewer_3Dmoljs' data-pdb='{}' data-backgroundcolor='0xffffff' data-style='stick' data-style1='cartoon:color=spectrum' data-spin='axis:y;speed:1' data-ui='true'></div>
    </div>
    """.format(id)

    # Render the HTML code using components.html
    components.html(html_code, width=500, height=500)
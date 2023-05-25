import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            st.write(
                '''
                <div style="display: flex; justify-content: space-between;">
                    <button style="margin-right: 25px;" onclick="closeModal()">Cancel</button>
                    <button onclick="redirectToLink()">OK</button>
                </div>
                <script>
                    function closeModal() {
                        // Close the modal
                        Streamlit.setComponentValue(false);
                    }
                    function redirectToLink() {
                        // Redirect to external link without opening in a new tab
                        window.location.href = "https://getdaniel.github.io/bc-drug/";
                    }
                </script>
                ''',
                unsafe_allow_html=True
            )
import streamlit as st
import streamlit.components.v1 as components


def help_page():
    # Importing the necessary CDNs
    st.markdown("""
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    """, unsafe_allow_html=True)

    # Show the modal when the button is clicked
    components.html("""
                    <div class="modal" tabindex="-1" role="dialog">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">Logout Confirmation</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <p>Are you sure you want to logout?</p>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
                                    <button id="logout-btn" type="button" class="btn btn-primary">Logout</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <script>
                        // Add event listener to the Logout button
                        document.getElementById('logout-btn').addEventListener('click', function() {
                            // Redirect to the new link
                            window.location.href = 'https://example.com'; // Replace with your desired link
                        });
                    </script>
                    """, height=0)

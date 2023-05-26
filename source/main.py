import streamlit as st
import streamlit.components.v1 as components
from streamlit_modal import Modal

from source.feedback import handle_user_feedback
from source.logout import handle_logout
from source.history import handle_history
from source.settings import handle_settings
from source.new import on_new_web_button_click
from source.XYZ_view import show_3d_visualization


def main():
    # Set page title and icon
    st.set_page_config(page_title="Drug Discovery", page_icon="assets/images/bio_logo.png")

    # Hide custom made with streamlit
    hide_made_with = """
                    <style>
                        footer {visibility: hidden;}
                    </style>
                     """
    st.markdown(hide_made_with, unsafe_allow_html=True)

    # Side bar
    st.markdown(
        """
       <style>
            [data-testid="stSidebar"][aria-expanded="true"]{
               min-width: 200px;
               max-width: 200px;
           }
        """,
        unsafe_allow_html=True,
    )
    # Create a placeholder for the page content
    page_placeholder = st.empty()

    # Add buttons to sidebar
    if st.sidebar.button("New", use_container_width=True):
        on_new_web_button_click()

    # Create the sidebar 3D View button
    if st.sidebar.button("3D View", use_container_width=True):
        # Remove previous page content
        page_placeholder.empty()
        show_3d_visualization()

    setting_modal = Modal("Settings", key="settings_button")
    if st.sidebar.button("Settings", use_container_width=True):
        setting_modal.open()

    handle_settings(setting_modal)

    feedback_modal = Modal("Feedback", key="feedback_button")
    if st.sidebar.button("Feedback", use_container_width=True):
        feedback_modal.open()

    handle_user_feedback(feedback_modal)

    history_modal = Modal("History", key="history_button")
    if st.sidebar.button("History", use_container_width=True):
        history_modal.open()

    handle_history(history_modal)

    logout_modal = Modal("Logout", key="logout_button")
    if st.sidebar.button("Log Out", use_container_width=True):
        logout_modal.open()

    handle_logout(logout_modal)
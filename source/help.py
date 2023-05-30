import streamlit as st
import streamlit.components.v1 as components

def help_page(modal):
    if modal.is_open():
        with modal.container():
            components.html("""
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>

                <!-- Modal -->
                <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-scrollable">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="staticBackdropLabel">Drug Discovery using AI for Breast Cancer</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <h6>Tips for Drug Discovery using AI for Breast Cancer:</h6>
                                <ul>
                                    <li>Collect and preprocess breast cancer data.</li>
                                    <li>Apply machine learning algorithms for feature selection and classification.</li>
                                    <li>Implement deep learning models for image analysis and diagnosis.</li>
                                    <li>Validate and evaluate the performance of the AI models using appropriate metrics.</li>
                                    <li>Optimize the models for improved accuracy and efficiency.</li>
                                    <li>Collaborate with domain experts to interpret and validate the results.</li>
                                </ul>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary">Understood</button>
                            </div>
                        </div>
                    </div>
                </div>
            """)
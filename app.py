import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Generate some random data
np.random.seed(123)
data = pd.DataFrame({
    'x': pd.date_range('2022-01-01', periods=365),
    'y': np.random.randn(365).cumsum()
})

# Create a line chart using Altair
chart = alt.Chart(data).mark_line().encode(
    x='x',
    y='y'
).properties(
    width=800,
    height=400
)

# Display the chart in the Streamlit app
st.altair_chart(chart)

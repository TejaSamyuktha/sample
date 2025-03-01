import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Sample Streamlit App")

# Create a random dataframe
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

# Display the dataframe as a table
st.write(data)

# Line chart
st.line_chart(data)

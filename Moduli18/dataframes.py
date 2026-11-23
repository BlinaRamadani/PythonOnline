import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFreame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age':[24, 22, 32, 29, 25],
    'City':['New York', 'Los Angeles','Chicago', 'Huoston', 'Phoenix']
})

st.dataframe(data)
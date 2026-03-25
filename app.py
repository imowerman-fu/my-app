import streamlit as st
import pandas as pd

st.title("This is my app")
st.write("This is a simple Streamlit app that displays a DataFrame.")   

data = {
    'Product': ["Product A", "Product B", "Product C"],
    'Sales': [100, 150, 200]
}

df = pd.DataFrame(data)

st.subheader("Sales Data")
st.dataframe(df)

st.subheader("Sales Chart")
st.bar_chart(df.set_index('Product')['Sales'])
import streamlit as st
import pandas as pd
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fb2b53;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header with logo + title ---
col_title , col_logo = st.columns([3, 1])

with col_logo:
    st.image("logo.jpeg", width=80)  # replace with your logo path or URL

with col_title:
    st.title("This is my app")

name = st.sidebar.text_input("Enter your name")
st.markdown(
    "<p style='font-size:30px;'>This is a simple Streamlit app that displays a DataFrame.</p>",
    unsafe_allow_html=True
)

if name:
    st.markdown(
        f"<p style='font-size:30px;'>Hello, {name}!</p>",
        unsafe_allow_html=True
    )
    
data = {
    'Product': ["Product A", "Product B", "Product C" , 'Product D' , 'Product E'],
    'Sales': [100, 150, 200, 250, 300] ,
    'Region': ['North', 'South', 'East', 'West', 'Central']
}

df = pd.DataFrame(data)

st.sidebar.header("User Input")
region = st.sidebar.selectbox("Select a region", ['All'] + list(df['Region'].unique()))



if region == 'All':
    filtered_df = df
else:
    filtered_df = df[df['Region'] == region]
   
col1, col2 = st.columns(2)
with col1:
    st.subheader("Sales Data")
    st.dataframe(filtered_df)
 
with col2:
    st.subheader("Sales Chart")
    st.bar_chart(df.set_index('Product')['Sales'])
    
    

import streamlit as st
import pandas as pd
import numpy as np

#Title of the appliction

st.title("My First Streamlit Application")

##Display a simple text
st.write("Hello, welcome to my first Streamlit application!")

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

##Display a dataframe
st.write(df)

line_chart=pd.DataFrame(
    np.random.randn(20,3),columns=['b','a','c']

)
st.line_chart(line_chart)
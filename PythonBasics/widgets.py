import pandas as pd
import streamlit as st

st.title("Streamlit text input")
name=st.text_input("Enter your name")

st.write(f"Hello {name}!")

age=st.slider("Enter your age",0,100,25)
st.markdown("_Markdown_")
st.write(f"Your age is {age} years old")

options=["java","python","c++","javascript"]
language=st.selectbox("Select your favorite programming language",options)
st.write(f"Your favorite programming language is {language}")

data={
    "name":["Smita","Vinod","Dhruv","Anand"],
    "Age":[25,30,35,40],
    "City":["Pune","Mumbai","Delhi","Bangalore"]
}

df=pd.DataFrame(data)
file=df.to_csv("SampleData.csv",index=False)
st.write(df)

upload_file=st.file_uploader("Upload a CSV file",type=["csv"])
if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)


with st.form("My form"):
    userName=st.text_input("Enter your name")
    password=st.text_input("Enter your password")

    submit_button=st.form_submit_button("Submit")

    if submit_button:
        st.write(f"Welcome {userName}!")
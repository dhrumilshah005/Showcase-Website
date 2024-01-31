import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Dhrumil Shah")
    content = """ My name is Dhrumil Shah. I am a full time Oracle ERP consultant and an
    amateur Python programmer with ambition to become a data scientist."""
    st.info(content)

write_content = """Below you can find some of the apps I have built in Python. 
Feel free to contact me."""

st.write(write_content)
col3, empty_col, col5 = st.columns([1.5,0.5,1.5])

with open("data.csv") as csv_file:
    df = pd.read_csv("data.csv",sep=";")
with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{int(index)+1}.png")
        st.write(f"[Source Code]({row['url']})")
with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{int(index) + 1}.png")
        st.write(f"[Source Code]({row['url']})")
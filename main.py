import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Dhrumil Shah")
    content = """ My name is Dhrumil Shah. I am a full time Oracle ERP consultant and an
    amateur Python programmer with ambition to become a data scientist."""
    st.info(content)

import streamlit as st
from send_email import send_email
import pandas as pd

with open("topics.csv") as flat_file:
    test = flat_file.readlines()
    test = test[1:]


st.title("Contact Me")
with st.form(key="contactmeform"):
    input_email = st.text_input("Your Email address",key="inputemail")
    input_action = st.selectbox("What topic do you want to discuss?",test,index=None)
    input_message = st.text_area("Please type a message")
    message=f"""\
Subject: New message from {input_email}

From : {input_email}
Topic: {input_action}
Message : {input_message}
"""
    button = st.form_submit_button()

    if button:
        if '@' in input_email and '@' in input_email and input_email and input_message:
            send_email(sender_message=message)
            st.info("You message has been submitted!")
        elif not '@' in input_email and not '.' in input_email and input_email:
            st.error("Please enter a valid email address and try again")
        elif not input_email:
            st.error("Please enter your email address and try again")
        elif not input_message:
            st.error("Please enter a message and try again")


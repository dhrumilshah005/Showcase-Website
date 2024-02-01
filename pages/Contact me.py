import streamlit as st

st.title("Contact Me")
with st.form(key="contactmeform"):
    input_email = st.text_input("Your Email address")

    input_message = st.text_area("Please type a message")
    button = st.form_submit_button()
    if button:
        if '@' in input_email and '@' in input_email and input_email and input_message:
            st.write("You message has been submitted!")
        elif not '@' in input_email and not '.' in input_email and input_email:
            st.error("Please enter a valid email address and try again")
        elif not input_email:
            st.error("Please enter your email address and try again")
        elif not input_message:
            st.error("Please enter a message and try again")


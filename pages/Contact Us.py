import streamlit as st
import pandas
import send_email

form = st.form(key="email_form")

with form:

    email = st.text_input("Your Email Adress")

    topic_options = pandas.read_csv("topics.csv")
    topic = st.selectbox('What topic do you want to discuss', topic_options["topic"])  # ["topic"] values for topic rows

    raw_message = st.text_area("Text")
    submit = st.form_submit_button("Submit")

    message = f"""\
Subject: new email from {email}

From: {email}
Topic: {topic}
{raw_message} 
"""

    if submit:
        send = send_email.send_email(message)
        if send == "error":
            st.info("you cant enter ř/í/ů.. characters")
        else:
            st.info("your email have been sent")

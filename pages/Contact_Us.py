import streamlit as st
from testsend import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address:")
    topic_related = st.selectbox("What topic do you want to discuss",("Job inquiries", "About the company", "business proposal"))
    user_message = st.text_area("Enter your message:")
    button = st.form_submit_button("Submit")
    message_sending_out = f"""\
Subject: New email from {user_email}

From: {user_email}
{topic_related}
{user_message}
        """
    
    if button:
        print(button)
        print(user_message)
        send_email(message_sending_out)
        print(message_sending_out)
        st.info("Email sent successfully!")
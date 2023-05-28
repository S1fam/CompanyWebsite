import smtplib
import ssl
import os


def send_email(message):
    try:
        host = "smtp.gmail.com"
        port = 465

        user = "s1fam0n3@gmail.com"  # change to your email if using
        password = os.getenv("PASSWORD1")  # the ones shown in previous commits have been changed :)
        # to create password you go to your gmail account and go to app passwords, generate one
        # and store it in user enviroment variable on your computer as PASSWORD1
        # when deploying on streamlit you can enter enviroment variable in advanced options
        reciever = "s1fam0n3@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            server.login(user=user, password=password)
            server.sendmail(user, reciever, message)
    except UnicodeError:
        return "error"


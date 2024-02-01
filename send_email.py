import smtplib, ssl
import os

def send_email(sender_message):
    host = "smtp.gmail.com"
    port = 465
    username = "dhrumil.ce@gmail.com"
    password = "scbw mcxg cuoo kuwu"
    receiver = "dhrumil.ce@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,sender_message)

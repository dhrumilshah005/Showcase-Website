import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "dhrumil.ce@gmail.com"
password = "scbw mcxg cuoo kuwu"
receiver = "dhrumil.ce@gmail.com"
context = ssl.create_default_context()
user_message = "Hello I need to connect with you "
message = """\
Subject: Email from Porfolio Website!
""" + user_message
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)

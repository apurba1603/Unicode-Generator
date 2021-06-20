import smtplib
from email.message import EmailMessage

msg=EmailMessage()
msg['Subject']='Books to be return immediately'
msg['From']='Asutosh College Library'
msg['To']='mca2020024@rcciit.org.in'

with open('EmailTemplate.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)
try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login('Email@gmail.com','Password')
        server.send_message(msg)
        print("Mail Sent Successfully")
except Exception as e:
    print(e)
finally:
    server.quit()


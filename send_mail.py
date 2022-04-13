from cgitb import html
from email import message
from email.mime.text import MIMEText
from http import server
from smtplib import SMTP
from email.message import EmailMessage
from config import settings
from email.mime.multipart import MIMEMultipart

def send_validate_email(user,title,body):
    message = MIMEMultipart()

    message['subject'] = title
    message['from'] = 'ycguevara89@gmail.com'#emisor
    message['To'] = user
    enviarHTML = MIMEText(body, 'html')
    message.attach(enviarHTML)

    username = settings.SMTP_USERNAME
    password = settings.SMTP_PASSWORD

    server = SMTP(settings.SMTP_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, user, message.as_string())

    server.quit()

import smtplib
import json
from pathlib import Path

# https://myaccount.google.com/apppasswords

def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    
    creds = {}
    with open(Path(__file__).parent / "credentials.json") as fp:
        creds = json.load(fp)
    email_from = creds["email_from"]
    email_to = creds["email_to"]
    key = creds["key"]

    # Authentication
    s.login(email_from, key)
    
    # sending the mail
    s.sendmail(email_from, email_to, message.encode('utf-8'))
    
    # terminating the session
    s.quit()
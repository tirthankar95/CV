import base64
import smtplib
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import json 
import re

def fill_body(name, company, body):
    file = open(f"{body}","r")
    replace_keys = ["<firstname>","<company>"]
    res_string = ""
    for line in file:
        for replace_key in replace_keys:
            if replace_key == "<firstname>": line = re.sub(replace_key, name, line)
            else: line = re.sub(replace_key, company, line)
        res_string += line 
    file.close() 
    return res_string

def send_email():
    file_email = open("JSON_AutomaticEmail.json", "r")
    detail_email = json.load(file_email)
    for r_idx, recipient in enumerate(detail_email['recipients']):
        msg = MIMEText(fill_body(recipient['name'], recipient['company'], recipient['body']))
        msg['Subject'] = recipient['subject']
        msg['From'] = detail_email['sender'] 
        msg['To'] = recipient['email']
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(detail_email['sender'], detail_email['password'])
            smtp_server.sendmail(detail_email['sender'], recipient['email'], msg.as_string())
        print(f"MSG SENT {detail_email['sender']} -->> {recipient['email']}")

if __name__ == '__main__':
    send_email()
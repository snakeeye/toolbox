#!/usr/bin/python3


import socket 
import smtplib
from email.message import EmailMessage
from email.header import Header
from email.mime.text import MIMEText
import os
import json

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)

def sendIpAddress(host, ip):
    with open('config.json') as json_file:
        data = json.load(json_file)
        sender = data["sender"]
        receiver = data["receiver"]
        mail_host = data["smtp_server"]
        mail_user = data["smtp_user"]
        mail_pass = data["smtp_pass"]

        print(sender + receiver + mail_host + mail_user + mail_pass)

        content = 'rt'
        title = "Host:" + host + " ip:" + ip
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = "{}".format(sender)
        message['To'] = "{}".format(receiver)
        message['Subject'] = title
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receiver, message.as_string())
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print (e)


sendIpAddress(hostname, IPAddr)

#!/usr/bin/env python3
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP
import getpass

def send_msg(host, port, pwd, sender, receivers, subject, msg):
    message = MIMEText(msg+'\r\n', _subtype='plain', _charset='utf8')
    message['From'] = Header(sender, charset='utf8')
    message['To'] = Header(receivers[0], charset='utf8')
    message['Subject'] = Header(subject, charset='utf8')

    smtp = SMTP(host=host, port=port)
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receivers, message.as_string())

    smtp.quit()


if __name__ == '__main__':
    host = 'smtp.163.com'
    port = 25
    pwd = 'spandy910827ying'
    sender = 'lijiying1991@163.com'
    receivers = ['lijiying1991@163.com']
    subject = 'Python Test Email for Internet'
    msg = 'python test email'

    send_msg(host, port, pwd, sender, receivers, subject, msg)
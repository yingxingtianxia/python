#!/usr/bin/env python3
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

def smail(sender, receivers, subject, msg, smtp_addr, port=25):
    message = MIMEText(msg+'\r\n', 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[1], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = SMTP(smtp_addr, port)
    smtp.sendmail(sender, receivers, message.as_string())


if __name__ == '__main__':
    sender = 'lijiying@tedu.cn'
    receivers = ['root@localhost', 'zhangsan@localhost']
    subject = 'Test Mail'
    msg = 'Python test mail for function'
    smtp_addr = '192.168.4.11'

    smail(sender, receivers, subject, msg, smtp_addr)
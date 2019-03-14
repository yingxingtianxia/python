#!/usr/bin/env python3
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

message = MIMEText('Python test mail\r\n', 'plain', 'utf8')
message['From'] = Header('ljy', 'utf8')
message['To'] = Header('root', 'utf8')
message['Subject'] = Header('Test mail', 'utf8')

sender = 'ljy@tedu.cn'
receivers = ['root@localhost', 'zhangsan@localhost']
smtp = SMTP('192.168.4.11', 25)
smtp.sendmail(sender, receivers, message.as_string())
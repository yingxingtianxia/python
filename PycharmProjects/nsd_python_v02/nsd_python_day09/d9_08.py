#!/usr/bin/env python
#--coding: utf8--
import socket

host = '127.0.0.1'
port = 21567
addr = (host, port)

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(addr)

while True:
    try:
        data = raw_input('>')
        c.send(data + '\r\n')
        print c.recv(1024)
    except (KeyboardInterrupt, EOFError, socket.error):
        break
c.close()
#!/usr/bin/env python3
#--*--coding: utf8--*--
import socket
import os

host = '127.0.0.1'
port = 12345
addr = (host, port)

count = str(os.stat('hosts').st_size)
count = bytes(count, encoding='utf8')

file = open('hosts', 'rb')
data = file.read()
file.close()

c = socket.socket()
c.connect(addr)
c.sendall(count)
c.sendall(data)
c.close()
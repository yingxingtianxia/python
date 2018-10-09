#!/usr/bin/env python3
#--*--coding: utf8--*--
import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)

c = socket.socket(type=socket.SOCK_DGRAM)
c.sendto(b'How are you?', addr)

data, serv_addr = c.recvfrom(1024)
print(str(data, encoding='utf8'))
c.close()
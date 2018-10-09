#!/usr/bin/env python3
#--*--coding: utf8--*--
import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)

cs = socket.socket()
cs.connect(addr)

cs.sendall(b'I C U')
print(str(cs.recv(1024), encoding='utf8'), end='')
cs.close()
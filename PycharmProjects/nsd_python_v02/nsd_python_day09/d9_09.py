#!/usr/bin/env python
#--coding: utf8--
import socket
import time

host = ''
port = 21567
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

while True:
    data, cli_addr = s.recvfrom(1024)
    s.sendto('[%s] %s' % (time.ctime(), data), cli_addr)

s.close()


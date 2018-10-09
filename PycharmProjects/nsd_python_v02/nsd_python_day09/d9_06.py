#!/usr/bin/env python
#--coding: utf8--
import socket

host = ''
port = 1234
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    cli_sock, cli_addr = s.accept()
    print 'Client connected from' , cli_addr
    while True:
        cli_sock.send('I C U\r\n')
        data = cli_sock.recv(1024)
        if data.strip() == '':
            break
        print data,
    cli_sock.close()

s.close()
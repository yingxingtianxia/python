#!/usr/bin/env python3
#--*--coding: utf8--*--
import socket

host = ''
port = 12345
addr = (host, port)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)
cli_soct, cli_addr = s.accept()
print('Client connnected from: ', cli_addr)
data = cli_soct.recv(1024)
print([data])
cli_soct.sendall(b'I 4 C U\r\n')
cli_soct.close()
s.close()
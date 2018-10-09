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

cli_sock, cli_addr = s.accept()
print('Client connected from: ', cli_addr)
count = cli_sock.recv(1024)
count = int(str(count, encoding='utf8'))

recr_cou = 0
tdata = ''
while True:
    data = cli_sock.recv(10)
    data = str(data, encoding='utf8')
    tdata += data
    recr_cou += 10
    if recr_cou >= count:
        break

print(tdata)

cli_sock.close()
s.close()
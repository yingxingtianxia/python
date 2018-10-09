#!/usr/bin/env python3
#--*--coding: utf8--*--
import os
import time
import socket

host = ''
port = 12345
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)


cli_sock, cli_addr = s.accept()
pid = os.fork()
if pid:
    os.waitpid(-1, 0)
    s.close()
else:
    print('Client connected from: ', cli_addr)

    while True:
        data = str(cli_sock.recv(1024), encoding='utf8')
        if data.strip() == '':
            cli_sock.close()
            break
        data = '[%s]: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), data)
        print(data)

        cli_sock.sendall(bytes(data, encoding='utf8'))
#!/usr/bin/env python3
#--*--coding: utf8--*--
import time
import os
import socket

host = ''
port = 21567
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)

while True:
    try:
        while True:
            result = os.waitpid(-1, 1)
            print(result)
            if result[0] == 0:
                break
    except OSError:
        pass

    cli_sock, cli_addr = s.accept()
    pid = os.fork()
    if pid:
        cli_sock.close()
    else:
        s.close()
        while True:
            data = str(cli_sock.recv(1024), encoding='utf8')
            if not data.strip():
                cli_sock.close()
                break
            data = '[%s]: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), data)
            print(data)
            cli_sock.sendall(bytes(data, encoding='utf8'))
        s.close()

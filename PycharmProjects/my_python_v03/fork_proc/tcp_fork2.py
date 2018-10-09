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

while True:
    try:
        cli_sock, cli_addr = s.accept()
    except KeyboardInterrupt:
        break
    pid = os.fork()
    if pid:
        result = os.waitpid(-1, 0)
        # while True:
        #     if result[1] == 0:
        #         break
        cli_sock.close()
    else:
        print('Client connceted from: ', cli_addr)
        while True:
            data = str(cli_sock.recv(1024), encoding='utf8')
            if not data.strip():
                s.close()
                break
            data = '[%s]: %s' % (time.strftime('%H:%M:%d'), data)
            print(data)
            cli_sock.sendall(bytes(data, encoding='utf8'))
            cli_sock.close()
s.close()

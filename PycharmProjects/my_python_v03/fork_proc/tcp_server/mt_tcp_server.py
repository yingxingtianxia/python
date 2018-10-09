#!/usr/bin/env python3
#__*__coding: utf8__*__
import time
import socket
import threading

host = ''
port = 12345
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(2)

def handle(cli_addr, cli_sock):
    print('Client connected from:', cli_addr)
    while True:
        data = str(cli_sock.recv(1024), encoding='utf8')
        if not data.strip():
            break
        data = '[%s]: %s' % (time.strftime('%H:%M:%S'), data)
        print(data)
        cli_sock.sendall(bytes(data, encoding='utf8'))
    cli_sock.close()

while True:
    try:
        cli_sock, cli_addr = s.accept()
    except KeyboardInterrupt:
        break
    t = threading.Thread(target=handle, args=(cli_addr, cli_sock))
    t.start()

s.close()
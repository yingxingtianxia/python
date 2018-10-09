#!/usr/bin/env python
#--coding: utf8--
import os
import socket
import sys
import time

host = ''
port = 21567
addr = (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    cli_sock, cli_addr = s.accept()
    pid = os.fork()
    if pid:
        cli_sock.close()
        while True:
            result = os.waitpid(-1, os.WNOHANG)
            if result[0] == 0:
                break
    else:
        s.close()
        while True:
            data = cli_sock.recv(1024).strip()
            if data == '':
                cli_sock.close()
                sys.exit(0)
            cli_sock.send("[%s] %s\n" % (time.ctime(), data))

s.close()
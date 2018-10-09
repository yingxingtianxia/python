#!/usr/bin/env python
#--coding: utf8--
import os
import sys
import socket
import time
import threading

host = ''
port = 54321
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

def work(cli_sock, cli_addr):
    while True:
        data = cli_sock.recv(1024).strip()
        if data == '':
            cli_sock.close()
            break
        cli_sock.send('[%s] %s\n' % (time.ctime(), data))

def main():
    while True:
        cli_sock, cli_addr = s.accept()
        t = threading.Thread(target=work, args=(cli_sock, cli_addr))
        t.setDaemon(True)
        t.start()
if __name__ == '__main__':
    main()
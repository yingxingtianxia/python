#!/usr/bin/env python
#--coding: utf8--
import sys
import time
import socket

s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_STREAM)
s.sendall('Welcome\n')

while True:
    data = s.recv(1024)
    if len(data) == 0:
        break
    s.sendall('you are connected from %s.\n' % str(s.getpeername()))
    s.sendall(data)
    s.sendall('the local time is %s.\n' % time.ctime())
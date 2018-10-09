#!/usr/bin/env python3
#--*--coding: utf8--*--
# def info(name, age):
#     print(name, age)
#
# info('bob', 24)
# info(name='bob', age=24)
# #info(24, name='bob')
# info(age=24, name='bob')
#
# def add(x, y):
#     return x+y
#
# print(add(3,4))
#
# ad = lambda x,y: x+y
# print(ad(3,5))
#
#
#
# import socket
#
# s = socket.socket(socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# def func(*args):
#     for i in args:
#         print(i)
#
# func(1,2,3)
# func(1,2,3,4,5)
#
# def func(**kwargs):
#     for key in kwargs.keys():
#         print('%s: %s' % (key, kwargs[key]))
#
# func(a=5, b=6)


#
# import socket
# import time
# host = ''
# port = 12345
# addr = (host, port)
#
# s = socket.socket()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(addr)
# s.listen(2)
#
# cli_sock, cli_addr = s.accept()
# print('Client connected from: ' , cli_addr)
# data = str(cli_sock.recv(1024), encoding='utf8')
# print(data)
# print('sleep 5')
# cli_sock.close()
# time.sleep(5)
#
# s.close()
#
# sum10 = 0
# i = 1
# while i <= 10:
#     sum10 += i
#     i += 1
# print(sum10)

import os
import sys
a = 10
pid = os.fork()
if pid:
    res = os.waitpid(-1, 1)
    print(res)
    a += 5
    print('in parent a is', a)
else:
    a += 10
    print('in child a is', a)
    sys.exit()
print(a)
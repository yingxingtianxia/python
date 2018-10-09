#!/usr/bin/env python3
#--*--coding: utf8--*--
import socket

host = '' #代表本机所有的IP地址
port = 12345  #应该选择大于1024的端口
addr = (host, port)

s = socket.socket()
#默认情况下，套接字被系统保留一分钟，程序结束后，一分钟内无法再次启动
#设置地址重用，程序结束后可以立即再次启动
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr) #绑定地址到套接字
s.listen(2)  #启动监听最多两个客户端，没啥用但是必须写
cli_sock, cli_addr = s.accept() #开始等待客户端连接
print('Client connected from', cli_addr)

data = cli_sock.recv(1024)  #一次最多接受1024个字节
print([data])
cli_sock.close()
s.close()

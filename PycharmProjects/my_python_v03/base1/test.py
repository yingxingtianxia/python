#!/usr/bin/env python3
#__*__coding: utf8__*__
import socket

def scanner(ip, port):
    try:
        b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b.connect((ip, port))
        print('[+]%d port/tcp open' % port)
    except:
        pass

def main(ip):
    for port in range(1, 100):
        scanner(ip, port)


if __name__ == '__main__':
    ip = str(input('ip address: '))
    main(ip)
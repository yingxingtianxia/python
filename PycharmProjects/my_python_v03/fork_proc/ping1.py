#!/usr/bin/env python3
#--*--coding: utf8--*--
import time
import subprocess

def ping(host):
    rc = subprocess.call('ping -c 2 %s > /dev/null' % host, shell=True)
    if rc == 0:
        return '%s: up' % host
    else:
        return '%s: down' % host

if __name__ == '__main__':
    hosts = ['192.168.32.%s' % i for i in range(1, 255)]
    start = time.ctime()
    for ip in hosts:
        print(ping(ip))
    end = time.ctime()
    print(end-start)
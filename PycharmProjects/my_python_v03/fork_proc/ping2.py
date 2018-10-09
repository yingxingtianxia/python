#!/usr/bin/env python3
#__*__coding: utf8__*__
import os
import sys
import subprocess

def ping(host):
    rc = subprocess.call('ping -c 2 %s > /dev/null' % host, shell=True)
    if rc == 0:
        return '%s: up' % host
    else:
        return '%s: down' % host


if __name__ == '__main__':
    hosts = ['192.168.32.%s' % i for i in range(1, 255)]
    for ip in hosts:
        pid = os.fork()
        if pid:
            os.waitpid(-1, 0)
        else:
            print(ping(ip))
            sys.exit()

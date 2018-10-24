#!/usr/bin/env python3
#__*__coding: utf8__*__
import threading
import subprocess

def ping(host):
    rc = subprocess.call('ping -c 2 %s > /dev/null' % host, shell=True)
    if rc == 0:
        print('%s: up' % host)
    else:
        print('%s: down' % host)


if __name__ == '__main__':
    hosts = ['192.168.32.%s' % i for i in range(1, 255)]
    for ip in hosts:
        t = threading.Thread(target=ping, args=(ip, ))
        t.start()
    print('done')
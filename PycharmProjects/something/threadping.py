#!/usr/bin/env python3
#__*__coding: utf8__*__
import subprocess
import threading

def ping(host):
    rc = subprocess.call(
        'ping -c 2 %s &> /dev/null' % host,
        shell=True
    )
    if rc:
        print('%s:down' % host)
    else:
        print('%s:up' % host)

if __name__ == '__main__':
    ips = ['192.168.232.%s' % i for i in range(1,255)]
    for ip in ips:
        t = threading.Thread(target=ping, args=(ip,))
        t.start()

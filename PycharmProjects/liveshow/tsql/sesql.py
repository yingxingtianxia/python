#!/usr/bin/env python3
import sys
import subprocess
import threading

def test_se(host, port, user, password):
    rc = subprocess.call(
        'mysql -h%s -P%s -u%s -p%s -e "show databases;" &> /dev/null' % (host,port,user,password),
        shell=True
    )

    if rc:
        print('no')
    else:
        print('yes')

if __name__ == '__main__':
    host = sys.argv[1]
    port = sys.argv[2]
    user = sys.argv[3]
    password = sys.argv[4]
    times = int(sys.argv[5])

    for i in range(times):
        t = threading.Thread(target=test_se(host,port,user,password))
        t.start()
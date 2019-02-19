#!/usr/bin/env python3
import sys
import paramiko
import threading
import os


def rcmd(host, cmd, port=22, username='root', password=1):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        password=password,
        username=username,
        port=port
    )
    stdin, stdout, stderr = ssh.exec_command(command=cmd)
    out = stdout.read().decode('utf8')
    err = stderr.read().decode('utf8')

    if out:
        print('[%s: OUT]:\n\t%s' % (host, out))
    if err:
        print('[%s: ERROR]:\n\t%s' % (host, err))

    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "command"' % sys.argv[0])
        sys.exit(11)

    ipfile = sys.argv[1]
    if os.path.isfile(ipfile):
        print('No such file: ', ipfile)

    cmd = sys.argv[2]
    with open(ipfile, 'r') as fobj:
        for ip in fobj:
            t = threading.Thread(target=rcmd, args=(ip.strip(), cmd))
            t.start()
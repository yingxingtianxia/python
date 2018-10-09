#!/usr/bin/env python3
#--*--coding: utf8--*--
import sys
import subprocess
import random
import string

all_str = string.ascii_letters + string.digits

def rand_pass(n=8):
    pwd = ''
    for i in range(n):
        char = all_str[random.randint(0,len(all_str)-1)]
        pwd += char

    return pwd

def add_user(username, password, filename):
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call("echo '%s' | passwd --stdin %s" % (password, username), shell=True)
    with open(filename, 'a+') as fobj:
        fobj.write('%12s : %10s' % (username, password))
        fobj.write('\n')


if __name__ == '__main__':
    username = sys.argv[1]
    password = rand_pass()
    filename = '/tmp/users.txt'
    add_user(username, password, filename)
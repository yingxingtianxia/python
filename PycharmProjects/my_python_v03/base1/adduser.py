#!/usr/bin/env python3
#--*--coding: utf8--*--
import sys
import subprocess
import string
import random

all_str = string.ascii_letters + string.digits

def rand_pass(n=8):
    pwd = ''
    for i in range(n):
        char = all_str[random.randint(0,len(all_str)-1)]
        pwd += char

    return pwd

def record_user(user, pwd):
    with open('pwd.txt', 'a+') as fobj:
        fobj.write('%-12s: %-8s' % (user, pwd))
        fobj.write('\n')

def add_user(user):
    a = subprocess.call('useradd %s' % user, shell=True)
    if a == 0:
        pwd = rand_pass()
        b = subprocess.call("echo '%s' | passwd --stdin %s" % (pwd, user), shell=True)
        if b == 0:
            record_user(user, pwd)
            return '添加用户成功'
        else:
            return '添加用户失败'
    else:
        return '创建用户失败'


if __name__ == '__main__':
    user = sys.argv[1]
    add_user(user)
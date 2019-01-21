#!/usr/bin/env python3
#__*__coding: utf8__*__
import subprocess

args = 'ls -l /root'
res = subprocess.getstatusoutput(args)
print(res)
for i in res:
    print(i)
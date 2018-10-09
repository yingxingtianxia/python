#!/usr/bin/env python3
#__*__coding: utf8__*__
import os
import sys

def hello():
    print('hello world')

for i in range(3):
    pid = os.fork()
    if not pid:
        hello()
        sys.exit()
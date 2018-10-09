#!/usr/bin/env python3
#--*--coding: utf8--*--
import os

print('start....')

pid = os.fork()
if pid:
    print('hello from parent')
else:
    print('hello from child')
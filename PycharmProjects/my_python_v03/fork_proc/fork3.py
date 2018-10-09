#!/usr/bin/env python3
#--*--coding: utf8--*--
import os
import time

pid = os.fork()
if pid:
    print('in parent sleeping...')
    print(os.waitpid(-1, 1))
    time.sleep(15)
    print('parent exit')
else:
    print('in child sleeping...')
    time.sleep(10)
    print('child exit')
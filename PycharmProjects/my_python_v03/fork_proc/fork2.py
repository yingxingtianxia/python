#!/usr/bin/env python3
#--*--coding: utf8--*--
import os
import time

pid = os.fork()
if pid:
    print('In parent')
    time.sleep(10)
    print('Parent exit')
else:
    for i in range(5):
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        print(now_time)
        time.sleep(1)
    print('Child exit')
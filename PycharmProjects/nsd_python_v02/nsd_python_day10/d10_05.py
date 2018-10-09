#!/usr/bin/env python
#--coding: utf8--
import os
import time

for i in range(5):
    pid = os.fork()
    print pid
    if pid:
        print 'In parent'
        time.sleep(15)
        print 'parent exit'
    else:
        print 'In child'
        for i in range(5):
            print time.ctime()
            time.sleep(1)
        print 'child exit'
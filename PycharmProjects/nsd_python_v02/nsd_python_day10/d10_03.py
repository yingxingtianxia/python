#!/usr/bin/env python
#--coding: utf8--
import sys
import time

print 'Welcome'
while True:
    print 'Please enter a string:'
    sys.stdout.flush()
    line = sys.stdin.readline().strip()
    if len(line) == 0:
        break
    print 'you entered [%s] %s' % (time.ctime(), line)
#!/usr/bin/env python
#--coding: utf8--
import os
import time

def reap():
    result = os.waitpid(-1, os.WNOHANG)
    print 'Reaped child process %d' % result[0]

pid = os.fork()

if pid:
    print 'In parent, Sleeping 15s...'
    time.sleep(15)
    reap()
    time.sleep(5)
    print 'Parent Done'
else:
    print 'In Child, Sleep 5s...'
    time.sleep(5)
    print 'Child Done'
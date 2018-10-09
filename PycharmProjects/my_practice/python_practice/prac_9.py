#!/usr/bin/env python
#--coding: utf8--
import time

count = 0
while True:
    if count == 5:
        break
    else:
        print 'Hello World!'
        time.sleep(1)
        count += 1
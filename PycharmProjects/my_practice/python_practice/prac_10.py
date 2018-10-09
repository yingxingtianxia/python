#!/usr/bin/env python
#--coding: utf8--
import time

count = 0
while True:
    if count == 5:
        break
    else:
        print time.strftime('%Y-%m-%d  %H:%M:%S')
        time.sleep(1)
        count += 1
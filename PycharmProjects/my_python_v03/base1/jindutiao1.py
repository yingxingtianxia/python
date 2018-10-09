#!/usr/bin/env python3
#--*--coding: utf8--*--
import time

flag = ['/', '-', '\\', '|']

i = 0
while True:
    print("\r%s" % flag[i], end="")
    i += 1
    time.sleep(1)
    if  i == 4:
        i = 0
#!/usr/bin/env python3
#--*--coding: utf8--*--
import time

i = 0
while True:
    left = '#' * i
    right = '#' * (20 - i )
    print("\r%s@%s" % (left, right), end="")
    i += 1
    time.sleep(0.5)
    if i == 21:
        i = 0
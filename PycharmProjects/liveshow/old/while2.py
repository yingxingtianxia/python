#!/usr/bin/env python3
#__*__coding: utf8__*__
import  time
i = 0
while True:
    left = '#' * i
    right = '#' * (10 - i)
    print('\r%s@%s'  % (left, right), end  = '')
    time.sleep(0.5)
    i += 1
    if i == 11:
        i = 0
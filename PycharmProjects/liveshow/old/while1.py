#!/usr/bin/env python3
#__*__coding: utf8__*__
import time
flag = ['-', '/', '|', '\\']
i = 0

while True:
    print('\r%s' % flag[i], end = '')
    time.sleep(0.5)
    i += 1
    if i == 4:
        i = 0
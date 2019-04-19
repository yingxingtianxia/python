#!/usr/bin/env python3
import time
import sys

flag = ['-','/','|','\\']

i = 0
while True:
    print("\r%s" % flag[i], end="")
    try:
        i += 1
        time.sleep(0.2)
    except KeyboardInterrupt as err:
        print('err', err)
        sys.exit()

    if i == 4:
        i = 0
#!/usr/bin/env python3

import time
import sys


i = 0
while True:
    left = '#' * i
    right = '#' * (50-i)
    print("\r%s@%s" % (left, right), end="")
    i = i + 1
    try:
        time.sleep(0.2)
    except KeyboardInterrupt:
        print()
        sys.exit()
    if i == 51:
        i = 0


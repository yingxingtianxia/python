#！/usr/bin/env python3
#--*--coding: utf8--*--
import time

for i in range(1,11):
    print(i)
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('Bye')
        break
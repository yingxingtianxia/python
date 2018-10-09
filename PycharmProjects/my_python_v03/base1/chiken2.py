#!/usr/bin/env python3
#--*--coding: utf8--*--
import time

start = time.time()

for i in range(21):
    for j in range(34):
        k = 100-i-j
        if 5*i+3*j+k/3 == 100:
            print(i, j, k)

end = time.time()
running_time = end -start
print(running_time)
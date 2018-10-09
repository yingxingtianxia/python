#!/usr/bin/env python
#--coding: utf8--
i = 0
j = 1
k = 0

while i<5:
    k = 4 * j
    for i in range(5):
        if k%4 != 0:
            break
        else:
            i += 1
        k = k/4 * 5 + 1
    j += 1

print k
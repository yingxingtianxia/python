#!/usr/bin/env python
#--coding: utf8--
import numpy as np

for m in range(1,1001):
    n=[1]
    for i in range(2,m):
        if m % i == 0:
            n.append(i)
    if m == np.sum(n):
        print m
#!/usr/bin/env python
#--coding: utf8--
import numpy

a = list(numpy.random.randint(1, 100, 10))
print a

a.reverse()
print a

b = []
for i in range(1, len(a)+1):
    b.append(a[-i])
print b

print  b[-1::-1]
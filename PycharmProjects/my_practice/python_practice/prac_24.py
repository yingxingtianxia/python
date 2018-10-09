#!/usr/bin/env python
#--coding: utf8--
a = 1.0
b = 1.0
sum= 0.0
for i in range(1,11):
    a, b = b, a+b
    num = b/a
    sum += num

print sum
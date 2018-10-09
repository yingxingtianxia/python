#!/usr/bin/env python
#--coding: utf8--
with open('test_a.txt', 'r') as fobj:
    read_a = fobj.read()
with open('test_b.txt', 'r') as fobj:
    read_b = fobj.read()
with open('test_c.txt', 'w') as fobj:
    data = list(read_a+read_b)
    data.sort()
    strings = ''
    for i in data:
        strings += i

    fobj.write(strings)

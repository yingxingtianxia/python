#!/usr/bin/env python
#--coding: utf8--
with open('test.txt', 'a') as fobj:
    string = raw_input('请输入字符串：').upper()
    fobj.write(string)
    fobj.write('\n')

with open('test.txt', 'r') as fobj:
    print fobj.read()
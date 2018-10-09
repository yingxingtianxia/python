#!/usr/bin/env python3
#--*--coding: utf8--*--
import re

with open('testdata.txt') as fobj:
    data = fobj.read()

#print(data)

print(re.findall('\d{18}|\d{17}X', data))  #身份证号

print(re.findall('-?\d+\.\d+', data))  #浮点数

print(re.findall('[A-z][\w]{7,9}', data))
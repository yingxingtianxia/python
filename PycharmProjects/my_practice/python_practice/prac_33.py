#!/usr/bin/env python
#--coding: utf8--
import re

test_list = ['a', 'b', 'c', 'd', 'e',]
li = [1, 2, 3, 4, 5]
#one
str1 = ','.join(str(i) for i in test_list)
print str1
#two
# re_list = repr(li)[1,-1]
# print re_list
#three
m=re.search(r'\[(.*?)\]',li)
print m.groups()[0]
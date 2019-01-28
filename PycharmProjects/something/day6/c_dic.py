#!/usr/bin/env python3
#__*__coding: utf8__*__
import string
import random

strs = string.ascii_letters + string.digits + '@'
a_dic = {}

for i in range(1,11):
    len_value = random.randint(1,5)
    value = ''
    for j in range(1,len_value+1):
        value += random.choice(strs)
    a_dic[i] = value

with open('zidian.text','w') as fobj:
    fobj.write(str(a_dic))
#!/usr/bin/env python
#--coding: utf8--
import math
num = 1
while True:
    if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268)-int(math.sqrt(num + 268)) == 0:
        print '这个数字是%d'  % num
        break
    num += 1

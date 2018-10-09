#!/usr/bin/env python3
#--*--coding: utf8--*--
fobj = open('passwd')
for line in fobj:
    print(line, end="")
fobj.close()
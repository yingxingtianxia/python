#!/usr/bin/env python3
#--*--coding: utf8--*--
fobj = open('passwd')
while True:
    data = fobj.read(4096)
    if data == "":
        fobj.close()
        break
    print(data)
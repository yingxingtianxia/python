#!/usr/bin/env python3
#__*__coding: utf8__*__
# with open('passwd') as fobj:
#     data = fobj.read()
#     print(data)
with open('passwd') as fobj:
    data = fobj.readlines()
    print(data)
    for item in data:
        print(item,end='')
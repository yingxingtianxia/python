#!/usr/bin/env python3
#__*__coding: utf8__*__
filename = 'passwd'

# with open(filename) as fobj:
#     data = fobj.read(4)
#     print(data)
#     data2 = fobj.read(4)
#     print(data2)
#
# with open(filename) as fobj:
#     while True:
#         data = fobj.readline()
#         if data == "":
#             break
#         print(data,end="")
with open(filename) as fobj:
    data = fobj.readlines()
    for item in data:
        print(item,end="")


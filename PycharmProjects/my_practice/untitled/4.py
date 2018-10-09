#!/usr/bin/env python3
# -*-coding: utf8-*-
f = open('1.txt', 'rw+')
print('Name of the file: ' + f.name)
line = f.readline()
print('Read Line: '+ line)

f.seek(0, 0)
line = f.readline()
print('Read Line: '+ line)
f.close()
#!/usr/bin/env python3
# -*-coding: utf8-*-
file_name = 'test.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.rstrip())
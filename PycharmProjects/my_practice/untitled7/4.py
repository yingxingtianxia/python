#!/usr/bin/env python3
# -*-coding: utf8-*-
file_name = 'test.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
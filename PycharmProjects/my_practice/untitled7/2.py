#!/usr/bin/env python3
# -*-coding: utf8-*-
file_name = 'test.txt'
with open(file_name) as file_object:
    for  line in file_object:
        print(line.rstrip())
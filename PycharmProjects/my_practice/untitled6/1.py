#!/usr/bin/env python3
# -*-coding: utf8-*-
import json

numbers = [2, 3, 4, 5, 11, 14]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
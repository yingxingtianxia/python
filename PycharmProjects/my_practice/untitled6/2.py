#!/usr/bin/env python3
# -*-coding: utf8-*-
import json

file_name = 'numbers.json'
with open(file_name) as file_object:
    numbers = json.load(file_object)

print(numbers)
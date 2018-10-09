#!/usr/bin/env python3
# -*-coding: utf8 -*-
from name_founction import get_format_name

print('enter "q" at any time to quit')
while True:
    first = input('Please enter your first name: ')
    if first == 'q':
        break
    last = input('Please enter your last name: ')
    if last == 'q':
        break

    formated_name = get_format_name(first, last)
    print(formated_name)

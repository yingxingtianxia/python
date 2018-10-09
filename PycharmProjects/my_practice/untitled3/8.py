#!/usr/bin/env python3
# -*-coding: utf8-*-
def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = first_name + ' ' + middle_name + ' ' + last_name

    return full_name.title()

musician = get_formatted_name(first_name='li', middle_name='ji', last_name='ying')
print(musician)

musician = get_formatted_name(first_name='wang', last_name='wu')
print(musician)
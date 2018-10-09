#!/usr/bin/env python3
# -*-coding: utf8-*-
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name

    return full_name.title()

while True:
    print("Please tell me what's your name")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last_name: ")
    if l_name == 'quit':
        break

    format_name = get_formatted_name(f_name, l_name)
    print('\nHello' + format_name)
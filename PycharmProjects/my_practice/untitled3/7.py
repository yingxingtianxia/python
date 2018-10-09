#!/usr/bin/env python3
# -*-coding: utf8-*-
def get_formatted_name(first_name=input("please enter xing: "),
                       last_name=input('Please enter ming: ')):
    full_name = first_name + ' ' + last_name

    return full_name.title()


musician = get_formatted_name()
print(musician)
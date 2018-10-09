#!/usr/bin/env python3
# -*-coding: utf8-*-
def get_format_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' +last
    else:
        full_name = first + ' ' + last
    return full_name.title()


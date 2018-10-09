#!/usr/bin/env python
#--coding: utf8--
def cp_list(list):
    new_list = []
    for item in list:
        new_list.append(item)

    return new_list

if __name__ == '__main__':
    list = [1, 2, 3, 4]
    print cp_list(list)
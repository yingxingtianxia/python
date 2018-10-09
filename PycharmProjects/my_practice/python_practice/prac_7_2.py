#!/usr/bin/env python
#--coding: utf8--
import copy

def cp_list(list):
    new_list = copy.copy(list)

    return new_list

if __name__ == '__main__':
    old_list = [1, 2, 3, 4]
    print cp_list(old_list)
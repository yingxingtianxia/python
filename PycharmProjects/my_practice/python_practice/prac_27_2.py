#!/usr/bin/env python
#--coding: utf8--
#直接反转字符串
def back(strings):
    return strings[::-1]

if __name__ == '__main__':
    info = raw_input('Input strings: ')
    print back(info)
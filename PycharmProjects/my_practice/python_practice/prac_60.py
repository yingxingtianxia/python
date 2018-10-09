#!/usr/bin/env python
#--coding: utf8--
def count(strings):
    length = len(strings)
    print length

if __name__ == '__main__':
    strings = raw_input('请输入一串字符：')
    count(strings)
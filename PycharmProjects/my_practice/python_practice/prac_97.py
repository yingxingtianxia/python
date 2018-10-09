#!/usr/bin/env python
#--coding: utf8--
def in_out():
    filename = raw_input('请输入文件名：')
    data = ''
    with open(filename, 'a') as fobj:
        while data != '#':
            fobj.write(data)
            fobj.write('\n')
            data = raw_input('请输入字符串：')

if __name__ == '__main__':
    in_out()
#!/usr/bin/env python3
#--*--coding: utf8--*--
import os

def get_fname():
    while True:
        filename = input("请输入文件名：")
        if os.path.exists(filename):
            print('文件以存在')
        else:
            break

    return filename

def get_contents():
    contents = []
    while True:
        content = input("请输入内容（以end结尾）:")
        if content == 'end':
            break
        contents.append(content)

    return contents


def wfile(filename, contents):
    with open(filename, 'a+') as fobj:
        for line in contents:
            fobj.write(line)
            fobj.write('\n')


if __name__ == '__main__':
    fname = get_fname()
    contents = get_contents()
    wfile(fname, contents)
#!/usr/bin/env python3
# -*-coding: utf8-*-
# -*- coding: utf8 -*-

import os

def get_fname():    #得到文件名
    while True:
        fname = input("filename: ")
        if not os.path.exists(fname):
            break
        print ('%s already exists. Try another.' % fname)
    return fname

def get_content():   #得到内容
    content = []
    while True:
        line = input('(enter to end input)>')
        if line == '':
            break
        content.append(line)

    return content

def write_file(fname, content):
    fobj = open(fname, 'w')
    #with open(fname, 'w') as fobj:
    fobj.writelines(content)

def main():   #主程序
    fname = get_fname()
    content = get_content()
    data = ['%s\n' % line for line in content]
    write_file(fname, data)

if __name__ == '__main__':
    main()
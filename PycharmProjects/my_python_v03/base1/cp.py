#!/usr/bin/env python3
#--*--coding: utf8--*--
import sys

def py_cp(src_file, dst_file):
    f1 = open(src_file, 'rb')
    f2 = open(dst_file, 'wb')

    for line in f1:
    #    print(line)
        f2.write(line)
    # data = f1.read()
    # print(data)
    f1.close()
    f2.close()

if __name__ == '__main__':
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    py_cp(src_file, dst_file)
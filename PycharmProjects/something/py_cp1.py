#!/usr/bin/env python3
#__*__coding: utf8__*__
import sys

src_file = sys.argv[1]
dst_file = sys.argv[2]

with open(src_file,'rb') as sfobj:
    with open(dst_file,'ab') as dfobj:
        while True:
            data = sfobj.read(1024)
            if not data:
                break
            dfobj.write(data)
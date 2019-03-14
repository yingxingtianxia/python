#!/usr/bin/env python3
#__*__coding: utf8__*__
import sys

src_file = sys.argv[1]
dst_file = sys.argv[2]

with open(src_file,'rb') as f1:
    with open(dst_file, 'wb') as f2:
        while True:
            data = f1.read(1024)
            if not data:
                break
            f2.write(data)
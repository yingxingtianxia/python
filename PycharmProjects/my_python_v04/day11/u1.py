#!/usr/bin/env python3
import os
from urllib import request

def get_webpage(url, dst_file):
    if os.path.exists(dst_file):
        os.remove(dst_file)
    with open(dst_file, 'wb') as fobj:
        html = request.urlopen(url)
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)


if __name__ == '__main__':
    url = "http://www.baidu.com"
    dst_file = '/root/1.txt'
    get_webpage(url, dst_file)
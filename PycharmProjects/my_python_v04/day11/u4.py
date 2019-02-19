#!/usr/bin/env python3
from urllib import request
import os
import re

def get_web(url, dst_file):
    if os.path.exists(dst_file):
        os.remove(dst_file)
    with open(dst_file, 'wb') as fobj:
        html = request.urlopen(url)
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

def get_img_url(filename, patt):
    image_url_list = []
    cpatt = re.compile(patt)
    with open(filename, 'r') as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                item = m.group()
                image_url_list.append(item)

    return image_url_list


def get_image(img_path, img_list):
    if not os.path.exists(img_path):
        os.mkdir(img_path)

    for url in img_list:
        fname = url.split('/')[-1]
        fname = os.path.join(img_path, fname)
        try:
            get_web(url, fname)
        except:
            pass


        
if __name__ == '__main__':
    url = 'http://www.baidu.cn'
    dst_file = '/tmp/tedu.html'
    get_web(url, dst_file)
    patt = 'http://[\w./]+\.(jpg|png|jepg|gif)'
    img_list = get_img_url(dst_file, patt)
    img_path = '/tmp/images'
    get_image(img_path, img_list)

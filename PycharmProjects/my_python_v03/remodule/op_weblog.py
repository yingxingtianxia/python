#!/usr/bin/env python3
#--*--coding: utf8--*--
import re
import collections

def count_patt(fname, patt):
    counter = collections.Counter()
    cpatt = re.compile(patt)

    with open(fname, 'r') as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                counter.update([m.group()])

    return counter

if __name__ == '__main__':
    fname = 'web.log'
    ip_patt = '^(\d+\.){3}\d+'
    a = count_patt(fname, ip_patt)
    for key in a.keys():
        for key in a.keys():
            print('%s这个IP地址出现了%s次' % (key, a[key]))
    br_patt = 'Firefox|curl|ELinks'
    b = count_patt(fname, br_patt)
    for key in b.keys():
        print('%s这个浏览器出现了%s次' % (key, b[key]))
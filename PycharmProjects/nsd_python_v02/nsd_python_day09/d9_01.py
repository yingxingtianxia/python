#!/usr/bin/env python
#--coding: utf8--
import re

def count_patt(fname, patt):
    result = {}
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                result[key] = result.get(key, 0) + 1
    return result

def quick_sort(str_list):
    if len(str_list) == 0 or len(str_list) == 1:
        return str_list

    middle = str_list.pop()
    smaller = []
    larger = []

    for item in str_list:
        if item[-1] < middle[-1]:
            smaller.append(item)
        else:
            larger.append(item)

    return quick_sort(larger) + [middle] + quick_sort(smaller)

if __name__ == '__main__':
    log_file = 'web.log'
    ip = '(\d+\.){3}\d+'
    bw = 'Firefox|Chrome|ELinks|curl'
#    print count_patt(log_file, ip)
#    print count_patt(log_file, bw)
    a = count_patt(log_file, ip)
    print a
    print quick_sort(a.items())
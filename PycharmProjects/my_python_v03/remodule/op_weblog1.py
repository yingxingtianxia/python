#!/usr/bin/env python3
#--*--coding: utf8--*--
import re
import collections

class CountPatt():
    def __init__(self, fname, patt):
        self.fname = fname
        self.cpatt = re.compile(patt)
        self.counter = collections.Counter()

    def count(self):
        with open(self.fname, 'r') as fobj:
            for line in fobj:
                m = self.cpatt.search(line)
                if m:
                    self.counter.update([m.group()])

        return self.counter


if __name__ == '__main__':
    fname = 'web.log'
    ip_patt = '(\d+\.){3}\d+'
    c1 = CountPatt(fname, ip_patt)
    n1 = c1.count()
    for key in n1.keys():
        print('%s这个IP地址出现了%s次' % (key, n1[key]))
    br_patt = 'Firefox|curl|ELinks|Chrome'
    c2 = CountPatt(fname, br_patt)
    n2 = c2.count()
    for key in n2.keys():
        print('%s这个浏览器出现了%s次' % (key, n2[key]))
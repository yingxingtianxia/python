#!/usr/bin/env python
#--coding: utf8--
import re

class Counter(object):
    def __init__(self, patt):
        self.cpatt = re.compile(patt)
        self.patt_dict = {}

    def count_patt(self, filename):
        with open(filename) as fobj:
            for line in fobj:
                m = self.cpatt.search(line)
                if m:
                    key = m.group()
                    self.patt_dict[key] = self.patt_dict.get(key, 0) + 1

    def sort(self):
        alist = self.patt_dict.items()
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

            return quick_sort(smaller) + [middle] + quick_sort(larger)

        return quick_sort(alist)

if __name__ == '__main__':
    log_file = 'web.log'
    ip = '^(\d+\.){3}\d+'
    bw = 'Firefox|curl'
    c1 = Counter(ip)
    c1.count_patt(log_file)
    print c1.patt_dict
    print c1.sort()
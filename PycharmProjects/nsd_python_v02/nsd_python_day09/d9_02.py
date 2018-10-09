#!/usr/bin/env python
#--coding: utf8--
import re

class Counter(object):
    def __init__(self, filename):
        self.filename = filename

    def count_patt(self, patt):
        result = {}
        cpatt = re.compile(patt)

        with open(self.filename) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    result[key] = result.get(key, 0) + 1
        return result

if __name__ == '__main__':
    log_file = 'web.log'
    ip = '(\d+\.){3}\d+'
    bw = 'Firefox|ELinks|curl|Chrome'
    c = Counter(log_file)
    print c.count_patt(ip)
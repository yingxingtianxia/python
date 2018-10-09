#!/usr/bin/env python
#--coding: utf8--
def gen_block(fobj):
    lines = []
    counter = 0
    for line in fobj:
        lines.append(line)
        counter += 1
        if counter == 10:
            yield ''.join(lines)
            lines = []
            counter = 0

    if lines:
        yield ''.join(lines)

if __name__ == '__main__':
    fname = '/etc/passwd'
    with open(fname) as fobj:
        for block in gen_block(fobj):
            print block
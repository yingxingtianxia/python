#!/usr/bin/env python3
#--*--coding: utf8--*--
def gen_block(fobj):
    block = []
    lines = 0
    for line in fobj:
        block.append(line)
        lines += 1
        if lines == 10:
            yield block
            block = []
            lines = 0
    if block:
        yield block


if __name__ == '__main__':
    fname = '/etc/passwd'
    with open(fname) as fobj:
        for block in gen_block(fobj):
            print(block)
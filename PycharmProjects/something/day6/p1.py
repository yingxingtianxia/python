#!/usr/bin/env python3
#__*__coding: utf8__*__
import pickle
import sys

aset = {23,24,25}
bset = {'ab','ac','ad'}

with open('p1.txt', 'ab') as f:
    pickle.dump(aset,f)
    pickle.dump(bset,f)

with open('p1.txt', 'rb') as fobj:
    try:
        while True:
            data = pickle.load(fobj)
            print(data)
    except EOFError:
        sys.exit()
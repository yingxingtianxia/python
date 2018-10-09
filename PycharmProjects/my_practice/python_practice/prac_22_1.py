#!/usr/bin/env python
#--coding: utf8--

for a in ['x', 'y', 'z']:
    for b in ['x', 'y', 'z']:
        for c in ['x', 'y', 'z']:
            if a != b and b != c and c != a and a != 'x' and c != 'x' and c != 'z':
                print 'a vs %s\nb vs %s\nc vs %s' % (a,b,c)

for a in ['y', 'z']:
    for b in ['x', 'y', 'z']:
        for c in ['y']:
            if a != b and b != c and c != a:
                print 'a vs %s\nb vs %s\nc vs %s' % (a, b, c),
#!/usr/bin/env python
#--coding: utf8--
for i in range(10, 100):
    if 8 * i < 100 and 9 * i > 100:
        print i

        print '809*%s=800*%s+9*%s=%s' % (i,i,i,809*i)
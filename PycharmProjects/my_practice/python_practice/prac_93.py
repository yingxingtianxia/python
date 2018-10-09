#!/usr/bin/env python
#--coding: utf8--
import time

start = time.clock()
for i in range(10000):
    print i
end = time.clock()
print end - start


print 'different is %6.3f' % (end - start)
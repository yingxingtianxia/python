#!/usr/bin/env python
#--coding: utf8--
import time

start = time.time()
for i in range(3000):
    print i
end = time.time()
print end - start
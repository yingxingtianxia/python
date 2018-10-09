#!/usr/bin/env python
#--coding: utf8--
import hashlib

m = hashlib.md5()
with open('/bin/ls') as fobj:
    while True:
        data = fobj.read(4096)
        if data == '':
            break
        m.update(data)

print m.hexdigest()
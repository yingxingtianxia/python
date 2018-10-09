#!/usr/bin/env python3
#--*--coding: utf8--*--
import hashlib

hello = bytes('hello world', encoding='utf8')
m = hashlib.md5(hello)
print(m.hexdigest())
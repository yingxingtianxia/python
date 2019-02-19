#!/usr/bin/env python3
from urllib import request

r1 = request.quote('hello world')
print(r1)

r2 = request.unquote('hello%20world')
print(r2)
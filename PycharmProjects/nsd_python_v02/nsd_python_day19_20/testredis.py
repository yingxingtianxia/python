#!/usr/bin/env python3
#--*--coding: utf8--*--
import redis

r = redis.Redis(host='127.0.0.1', port=6379)

r.set("py17", 'hello')
print(r.get('py17'))
print(r.get("xi"))
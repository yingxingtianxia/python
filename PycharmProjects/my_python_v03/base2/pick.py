#!/usr/bin/env python3
#--*--coding: utf8--*--
import pickle
#
# adic = {'name':'zhangsan', 'age':25, 'sex':'male'}
# with open('user.txt', 'wb') as f:
#     pickle.dump(adic, f)


with open('user.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)
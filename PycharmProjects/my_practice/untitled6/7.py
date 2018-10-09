#!/usr/bin/env python3
# -*-coding: utf8-*-
goods = {'apple':{'price':8, 'number':1000}}
a = goods.keys()
b = goods.values()

for d in b:
    print(d['price'])
    print(d['number'])

for g in goods.keys():
    print('%s price is %d num is %d' % (g,goods[g]['price'],goods[g]['number']))
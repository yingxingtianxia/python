#!/usr/bin/env python3
# -*-coding: utf8-*-
cars = ['audi', 'baoma', 'dazhong','bieke']

for car in cars:
    if car == 'baoma':
        print(car.upper())
    else:
        print(car.title())
if 'dazhong' in cars:
    print('it is true')
if 'benchi' not in cars:
    print('it is true')

#!/usr/bin/env python3
# -*-coding: utf8-*-
def make_pizza(size, *toppings):
    print('\nMake a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)
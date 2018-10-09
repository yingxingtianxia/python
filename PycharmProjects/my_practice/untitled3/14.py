#!/usr/bin/env python3
# -*-coding: utf8-*-
def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + '-inch pizza with following toppings:')
    for topping in toppings:
        print('-' + topping)

make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green pepers', 'extra cheese')
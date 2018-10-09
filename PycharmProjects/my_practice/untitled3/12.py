#!/usr/bin/env python3
# -*-coding: utf8-*-
def print_modules(unprinted_desings, completed_modules):
    while unprinted_designs:
        current_disign = unprinted_designs.pop()
        print("Printing module: " + current_disign)
        completed_modules.append(current_disign)

def show_completed_modules(completed_modules):
    print("\nThe following modules have been printed: ")
    for completed_module in completed_modules:
        print(completed_module)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedrom']
completed_modules = []

print_modules(unprinted_designs, completed_modules)
show_completed_modules(completed_modules)
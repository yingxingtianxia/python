#!/usr/bin/env python3
# -*-coding: utf8-*-
def describe_pet(animal_type, pet_name):
    print('\nI have a ' + animal_type + '.' )
    print('My ' +animal_type + "'s name is " + pet_name.title() + '.')

active = True
while active:
    a_type = input('Please enter the type of the animal: ')
    if a_type == 'quit':
        break
        active = False
    else:
        P_name = input('Please enter the name of the animal: ')
        describe_pet(a_type, P_name)
#!/usr/bin/env python3
# -*-coding: utf8-*-
def describe_pet(pet_name, animal_type='dog'):
    print('\nI have a ' + animal_type.title() + '.')
    print('My ' + animal_type.title() + "'s name is " + pet_name.title() + '.')

describe_pet('willie')
describe_pet(pet_name='whllie')

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

describe_pet()
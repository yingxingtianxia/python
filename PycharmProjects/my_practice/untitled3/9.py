#!/usr/bin/env python3
# -*-coding: utf8-*-
def build_person(first_name, last_name, age=''):
    person = {'first':first_name, 'last':last_name, 'age':age}

    return person
musician = build_person('li', 'jiying','26')
print(musician)

musician = build_person('wang', 'wu')
print(musician)
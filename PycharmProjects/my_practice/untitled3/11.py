#!/usr/bin/env python3
# -*-coding: utf8-*-
def greet_users(names):
    for name in names:
        msg = "Hello " + name.title() + '.'
        print(msg)

usernames = ['harry', 'tom', 'kenji', 'natasha']
greet_users(usernames)
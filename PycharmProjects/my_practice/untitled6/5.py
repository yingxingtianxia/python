#!/usr/bin/env python3
# -*-coding: utf8-*-
import json

filename = 'usernamet.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('Please enter your name: ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print('we will remember you when you come back' + username)
else:
    print('welcome back ' + username)
#!/usr/bin/env python3
# -*-coding: utf8-*-
import  json

user_name = input('Please enter your name: ')

filename = 'username.json'
with open(filename, 'w') as fileobjcet:
    json.dump(user_name, fileobjcet)
    print('we will remember you when you come back' + user_name + '!')
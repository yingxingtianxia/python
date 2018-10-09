#!/usr/bin/env python3
# -*-coding: utf8-*-
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print('welcome back ' + username)
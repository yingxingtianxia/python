#!/usr/bin/env python3
# -*-coding: utf8-*-
import json

def get_stored_username():
    file_name = 'usernamete.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('Please enter your name: ')
    file_name = 'usernamete.json'
    with open(file_name, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print('welcome back' + username)
    else:
        username = get_new_username()
        print("we'll remember you when you come back")

greet_user()
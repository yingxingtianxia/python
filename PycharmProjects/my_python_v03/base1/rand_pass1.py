#!/usr/bin/env python3
#--*--coding: utf8--*--
import string
from random import randint

letters = string.ascii_letters + string.digits + string.punctuation

def rand_pass(n=8):
    password = ''
    while len(password) < n:
        num = randint(0, len(letters)-1)
        ran_str = letters[num]
        if ran_str in password:
            continue
        password = password + ran_str

    return password

if __name__ == '__main__':
    rand_pass()
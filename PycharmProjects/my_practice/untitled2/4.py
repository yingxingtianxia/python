#!/usr/bin/env python3
# -*-coding: utf8-*-
prompt = '\nTell me something and I will repeat it back to you.'
prompt += '\nEnter "quit" to stop the program.'

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
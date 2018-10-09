#!/usr/bin/env python3
# -*-coding: utf8-*-
prompt = '\nPlease input the name of a city you have visited.'
prompt += '\nEnter "quit" when you are finished.'

while True:
    city = input(prompt).title()

    if city == 'quit':
        break
    else:
        print('I would like to go to ' + city + '!')
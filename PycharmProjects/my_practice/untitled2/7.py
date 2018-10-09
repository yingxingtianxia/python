#!/usr/bin/env python3
#  -*-coding: utf8-*-
unconfirm_users = ['tom','kenji','natasha','chihiro']
confirmed_users = []

while unconfirm_users:
    current_user = unconfirm_users.pop()
    print('verifying user: ' + current_user.title())

    confirmed_users.append(current_user)

print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#!/usr/bin/env python3
# -*-coding: utf8-*-
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princetom',
                             field='physics')
print(user_profile)
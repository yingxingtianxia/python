#!/usr/bin/env python3
# -*-coding: utf8-*-
favorite_languages = {
    'jen':'python',
    'seach':'c',
    'kenji':'ruby',
    'chihiro':'html',
}
#print('Seach~s favorite language is '+ favorite_languages['seach'].title())
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +language.title())
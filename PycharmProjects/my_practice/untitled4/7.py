#!/usr/bin/env python3
# -*-coding: utf8-*-
from collections import OrderedDict

favorate_languages = OrderedDict()

favorate_languages['jen'] = "python"
favorate_languages['kenji'] = "c"
favorate_languages['natasha'] = "php"
favorate_languages["chihiro"] = "java"

for name, language in favorate_languages.items():
    print(name.title() + "'s favorate language is " + language.title())

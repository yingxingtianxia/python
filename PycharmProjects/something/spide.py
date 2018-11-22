#!/usr/bin/env python3
#__*__coding: utf8__*__
import json
import re

with open('1.txt') as fobj:
    data = json.load(fobj)
    print(data)
    print(data['NetworkSettings']['IPAddress'])
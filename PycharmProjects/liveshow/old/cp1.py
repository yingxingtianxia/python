#!/usr/bin/env python3
#__*__coding: utf8__*__
with open('passwd','r') as f1:
    with open('password','w') as f2:
        while True:
            data = f1.read(1024)
            if  data == "":
                break
            f2.write(data)
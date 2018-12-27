#!/usr/bin/env python3
#__*__coding: utf8__*__
with open('passwd','r') as fobj:
    with open('userinfo','w') as f:
        while True:
            data = fobj.read(1024)
            if data == "":
                break
            f.write(data)
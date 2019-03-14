#!/usr/bin/env python3
#__*__coding: utf8__*__
level = int(input("请输入等级："))
#level = int(level)
if 0 < level < 30:
    print('初级')
elif 30 <= level < 60:
    print('中级')
elif 60 <= level <= 100:
    print('高级')
else:
    print('输入非法')
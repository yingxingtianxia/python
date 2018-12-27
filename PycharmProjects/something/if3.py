#!/usr/bin/env python3
#__*__coding: utf8__*__
grade = input('请输入成绩：')
grade = int(grade)
if 80 <= grade <=100:
    print('优秀')
elif 60<= grade < 80:
    print('良好')
elif 0 <= grade <60:
    print('不及格')
else:
    print('分数非法')
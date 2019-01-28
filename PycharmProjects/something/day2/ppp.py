#!/usr/bin/env python3
#__*__coding: utf8__*__
adic = {
    'stu1':['zhangsan','15','class1'],
    'stu2':['lisi','14','class2'],
    'stu3':['wangwu','15','class3']
}

for id in adic.keys():
    stu_id = id
    stu_name  = adic[id][0]
    stu_age = adic[id][1]
    stu_class = adic[id][2]
    print(stu_id,stu_name,stu_age,stu_class)
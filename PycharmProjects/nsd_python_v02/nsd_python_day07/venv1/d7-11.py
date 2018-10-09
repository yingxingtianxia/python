#!/usr/bin/env python
#--coding: utf8--
def count(func):
    def times(**kwargs):
        return func(**kwargs) * 3
    return times

@count
def fm(name, age):
    return 'My name is %s and I am %s years old\n' % (name, age)

if __name__ == '__main__':
    dic = {'name':'tom', 'age':25}
    print fm(**dic)
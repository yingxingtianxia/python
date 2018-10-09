#!/usr/bin/env python3
#--*--coding: utf8--*--
def get_kwargs(**kwargs):
    print(kwargs)

def get_age(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_kwargs()
    get_kwargs(name='bob', age=25, gender='male')

    info = {'name':'bob', 'age':'25'}
    get_age(**info)
#!/usr/bin/env python3
#--*--coding: utf8--*--
def get_args(*args):
    print(args)


if __name__ == '__main__':
    get_args()
    get_args('zhangsan')
    get_args('zhangsan', 25)
    get_args('zhangsan', 25, 'male')
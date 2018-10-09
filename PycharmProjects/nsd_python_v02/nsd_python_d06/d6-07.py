#！/usr/bin/env python3
#--*--coding: utf8--*--
def get_info(name, age):
    print('%s is %s years old' % (name, age))

get_info('bob', 22)
get_info(22, 'bob')
get_info(age=22, name='bob')
#get_info(name='bob', 22)           #关键字参数必须在最后
#def func(name='bob', age)          #变量有默认值必须放最后
#get_info(23, name='bob')           #name变量得到多个值
#get_info('bob', 23, 24)            #实参个数与形参个数相等
get_info('bob', age=23)
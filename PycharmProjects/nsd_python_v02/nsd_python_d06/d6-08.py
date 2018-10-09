#！/usr/bin/env python3
#--*--coding: utf8--*--
def get_args(*args):
    print(args)

def get_kwargs(**kwargs):
    print(kwargs)

def get_info(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_args()
    get_args('abc')
    get_args(10, 20, 30, 40)
    get_kwargs()
    get_kwargs(name='bob', age=23)
    info = ['bob', 25]
    get_info(*info)
    info_dict = {'name': 'bob', 'age': 25}
    get_info(**info_dict)
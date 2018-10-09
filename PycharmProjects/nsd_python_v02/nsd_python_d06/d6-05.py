#！/usr/bin/env python3
#--*--coding: utf8--*--
def set_age(name, age):
    if not 0 < age < 150:
        raise ValueError('age out of range')        #触发
    print('%s is %d years old' % (name, age))

def set_age2(name, age):
    assert 0 < age < 150, 'age out of range'        #断言
    print('%s is %d years old' % (name, age))

if __name__ == '__main__':
    name = input('name: ')
    age = int(input('age: '))
    set_age(name, age)
    set_age2(name, age)
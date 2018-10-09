#!/usr/bin/env python
# --coding: utf8--
#闭包返回值是函数
def set_color(func):
    def set_red(*args):
        return '\033[31;1m%s\033[0m' % func(*args)

    return set_red


@set_color
def welcome(place):
    return 'welcome to %s' % place


@set_color
def say_hi():
    return 'How are you?'


if __name__ == '__main__':
    print welcome('Beijing')
    print say_hi()

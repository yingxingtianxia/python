#!/usr/bin/env python
#--coding: utf8--
from random import randint

def link_list(n=5):
    link_list = []
    for i in range(n):
        link_list.append(randint(1,100))

    return link_list

def back_link_list(link_list):
    link_list.reverse()
    return link_list
if __name__ == '__main__':
    ll = link_list()
    print ll
    print back_link_list(ll)
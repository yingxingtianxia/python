#!/usr/bin/env python
#--coding: utf8--
def baoshu(n=5):
    a_list = [i+1 for i in range(n)]
    print a_list

    i = 1
    while len(a_list) > 1:
        if i % 3 == 0:
            a_list.pop(0)
        else:
            # a_list.insert(len(a_list), a_list.pop(0))
            a_list.append(a_list.pop(0))
        i += 1
    print a_list

if __name__ == '__main__':
    baoshu()
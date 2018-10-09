#!/usr/bin/env python
#--coding: utf8--
def baoshu(n=5):
    a_list = [i+1 for i in range(n)]
    print a_list
    sum = 0
    while True:
        t = 0
        for i in range(1, len(a_list)+1):
            sum += 1
            if sum%3 == 0:
                a_list.pop(i-1-t)
                t += 1

        if len(a_list) == 1:
            print a_list[0]
            break

if __name__ == '__main__':
    baoshu(3)
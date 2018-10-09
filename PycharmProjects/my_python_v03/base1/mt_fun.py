#!/usr/bin/env python3
#--*--coding: utf8--*--
def gen_tab(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('%s * %s = %s' % (j, i, i*j), end=" ")
        print()

    return n

if __name__ == '__main__':
    count = int(input("请输入行数："))
    gen_tab(count)
    print("行数是：", gen_tab(count))
#!/usr/bin/env python3
#--*--coding: utf8--*--
def gen_fib(n):
    fiber = [0, 1]
    for i in range(n-2):
        new_num = fiber[-1] + fiber[-2]
        fiber.append(new_num)
    print(fiber)

    return fiber

if __name__ == '__main__':
    fib_len = int(input("请输入数列长度："))
    gen_fib(fib_len)

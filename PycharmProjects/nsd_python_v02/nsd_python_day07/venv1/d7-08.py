#!/usr/bin/env python
#--coding: utf8--
import time

def deco(func):
    def timeit():
        start = time.time()
        ret_va = func()
        end = time.time()
        return ret_va,  end - start
    return timeit

@deco
def loop():
    result = []
    for i in range(1, 11):
        result.append(i)
        time.sleep(0.1)
    return result


if __name__ == '__main__':
    print loop()
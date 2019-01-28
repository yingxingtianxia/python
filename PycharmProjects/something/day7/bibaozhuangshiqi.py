#!/usr/bin/env python3
#__*__coding: utf8__*__
import time

def deco(func):
    def timeit():
        start = time.time()
        result = func()
        end = time.time()
        run_time = end - start
        return run_time, result
    return timeit

@deco
def loop():
    result = []
    for i in range(10):
        result.append(i)
        time.sleep(0.5)
    return result

if __name__ == '__main__':
    print(loop())
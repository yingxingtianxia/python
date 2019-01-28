#!/usr/bin/env python3
import requests
import pprint
import time


def run_time(func):
    def timeit(n):
        start = time.time()
        res = func(n)
        end = time.time()

        return end-start,res
    return timeit

@run_time
def get_weather(number):
    url = "http://www.weather.com.cn/data/zs/%s.html"
    r = requests.get(url % (number,))
    r.encoding = "utf-8"
    data = r.json()

    return data

if __name__ == '__main__':
    d = get_weather(101010400)
    pprint.pprint(d)

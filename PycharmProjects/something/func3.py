#!/usr/bin/env python3
import requests
import pprint
import time

def run_time(func):
    def timeit(n):
        start = time.time()
        res = func(n)
        end = time.time()

        return end - start,res
    return timeit

@run_time
def get_weather(number):
    url_get = 'http://www.weather.com.cn/data/zs/%s.html'
    response = requests.get(url_get % (number))
    response.encoding = 'utf-8'
    data = response.json()

    return data


if __name__ == '__main__':
    data = get_weather(101010400)
    pprint.pprint(data)
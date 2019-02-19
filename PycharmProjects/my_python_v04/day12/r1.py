#!/usr/bin/env python3
from urllib import request
import json
import pprint

weather_url = 'http://www.weather.com.cn/data/sk/101010100.html'
info_url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
zs_url = 'http://www.weather.com.cn/data/zs/101010100.html'

weather_data = request.urlopen(weather_url).read()
info_data = request.urlopen(info_url).read()
zs_data = request.urlopen(zs_url).read()

pprint.pprint(json.loads(weather_data))
print('#' * 50)
pprint.pprint(json.loads(info_data))
print('#' * 50)
pprint.pprint(json.loads(zs_data))


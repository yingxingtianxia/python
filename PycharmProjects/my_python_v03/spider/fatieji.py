#!/usr/bin/env python3
#__*__coding: utf8__*__
from pyquery import PyQuery as pq
import requests

url = 'http://127.0.0.1:8000/blog/add'
s = requests.Session()
response = s.get(url)
# print(response.text)
doc = pq(response.text)
inputVal = doc('input[name="csrfmiddlewaretoken"]').val()
# print(inputVal)

data = {
    'csrfmiddlewaretoken': inputVal,
    'title' : 'requests post title',
    'desc': 'requests post dic',
    'author': 'requtest',
    'content': 'content',
}

s.post(url, data=data)
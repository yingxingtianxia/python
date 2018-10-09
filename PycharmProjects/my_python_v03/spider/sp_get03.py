#!/usr/bin/env python3
#__*__coding: utf8__*__
import urllib.request
import urllib.parse

url = 'http://127.0.0.1:8888'
header = {
'Cookie' :'csrftoken=1apNKPPhJR1378tMGl5o5ovJHxkV8WKpxqgqfvRouWXpKi3dqPlYpjvN5UCSxqfa; sessionid=dcn0up6ms6laahbpn1i10fe9l1qi7w9u; uid="2|1:0|10:1537329167|3:uid|8:YWRtaW4=|10898dd06d490faecfc6d259aa9b3373af41476d51ac6b6cbbf495664a7272ee"'
}

request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request).read()

print(response)
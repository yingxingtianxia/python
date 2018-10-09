#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests

url = 'http://jeasyui.com/demo/main/datagrid2_getdata.php'
s = requests.Session()
data = {'page':1, 'rows':30}
response = s.post(url, data=data)

print(response.json())




#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests

url = 'http://ttsconsole.tmooc.cn/index'

headers = {
    'Cookie':'Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1536629297; JSESSIONID=787F4DBC087BF41EA846737534CCD2BB; tedu.local.language=zh-CN'
}
response = requests.get(url, headers=headers)
print(response.text)
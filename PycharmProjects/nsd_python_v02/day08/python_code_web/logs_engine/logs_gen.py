#!/usr/bin/python
# coding=utf-8

"""
程序模拟了Android等APP记录前端用户访问行为
日志记录的关键信息可以定义为这样一句话:
某人,在某个地方,某个时刻,通过某种终端的某个应用,对某个目标,做了什么
某人:为注册用户的ID
某个地方:用户访问的IP
某个终端:MAC地址,设备标识等
某个应用:APP的名称,版本
某个目标:电影,歌曲,按钮,特定页面等
做了什么:播放,打开,点击,保存,下载, 页面流转等

日志记录的标准方式为HTTP,利用nginx的日志功能进行记录
可以方便的定义日志的格式
本程序以随机方式,定义了一些随机访问行为
"""
import random
from urllib import urlopen

mac = ['32:00:10:05:59:e1', '32:00:10:05:59:e2', '32:00:10:05:59:e3', '32:00:10:05:59:e4', '32:00:10:05:59:e5']
device = ['iphone', 'samsung', 'skyworthTV', 'XiaomiTV', 'HTC3001']
app = ['kuwoMobilePLayer', 'kuwoTVKtv', 'kuwoPcPlayer', 'kuwoTvRadio', 'kuwoMobileKTV']
ver = ['2.0.1', '5.5.6', '2.1.4', '10.4.5', '6.1.13']
content = ['song103', 'song213', 'song301', 'song302', 'song234', 'song478']
act = ['play', 'save', 'download', 'like', 'share']


def randstr(list=[]):
    count = len(list)
    index = random.randint(0, count - 1)
    return str(list[index])


def randUser():
    return "u%03d" % random.randint(0, 299)


host = "http://192.168.99.100:40080/log/"

nlogs = 3000

for i in range(nlogs):
    log = host + randUser() + "/" + randstr(mac) \
          + "/" + randstr(device) + "/" + randstr(app) + "/" + randstr(ver) + "/" \
          + randstr(act) + "/" + randstr(content) + "/"
    urlopen(log)
    print "send log =", i

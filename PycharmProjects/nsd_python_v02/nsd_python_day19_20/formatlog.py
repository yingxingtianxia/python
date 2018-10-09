#!/usr/bin/env python3
#--*--coding: utf8--*--
import datetime
import time
from random import randint

# org = '[127.0.0.1][16/Jul/2018:12:06:05 +0800]' \
#       '[/loggen/u088/32:00:04:5a:34:22/skyworthTV/kuwoMobilePLayer/2.1.4/play/song213][user]'
# org = org.replace(']', " ")
# chg = org.split('[')
# print(chg)
# ip = chg[1]
# stime = chg[2]
# uri = chg[3]
# print(ip, stime, uri)
#
# stime = stime.split(" ")[0]
# dtime = datetime.datetime.strptime(stime, '%d/%b/%Y:%H:%M:%S')
# dtime = time.mktime(dtime.timetuple())
# dtime = int(dtime)
# print(dtime)
#
# uri = uri.split('/')
# print(uri)
# uid = uri[2]
# mac = uri[3]
# dev = uri[4]
# app = uri[5]
# ver = uri[6]
# act = uri[7]
# content = uri[8]
#
# print(uid, mac, dev, app, ver, act, content)
#
#
#
def format(org):
    # org = org.replace(']', "")
    # chg = org.split('[')
    # ip = chg[1]
    # stime = chg[2]
    # uri = chg[3]

    ips = ['32.192.107.21', '202.204.48.83', '217.32.18.19', '147.45.67.98', '9.32.193.111']
    ip = ips[int(randint(0, len(ips)-1))]

    times = ['16/Jul/2018:12:06:05', '17/Aug/2018:18:06:26',
             '22/Feb/2017:06:24:15', '30/Nov/2018:10:43:35', '02/Dec/2018:14:43:36']
    stime = times[int(randint(0, len(times)-1))]
    dtime = datetime.datetime.strptime(stime, '%d/%b/%Y:%H:%M:%S')
    dtime = time.mktime(dtime.timetuple())
    dtime = int(dtime)
    # stime = stime.split(" ")[0]
    # dtime = datetime.datetime.strptime(stime, '%d/%b/%Y:%H:%M:%S')
    # dtime = time.mktime(dtime.timetuple())
    # dtime = int(dtime)
    org = org.replace(']', "")
    chg = org.split('[')
    uri = chg[3]
    uri = uri.split('/')
    uid = uri[2]
    mac = uri[3]
    dev = uri[4]
    app = uri[5]
    ver = uri[6]
    act = uri[7]
    content = uri[8]

    std_format = '%s/%s/%s/%s/%s/%s/%s/%s/%s/' % (dtime, ip, dev, mac, uid, app, ver, act, content)
    return std_format

def format_log(filename_org, filename_chg):
    with open(filename_org) as fobj:
        org = fobj.readline()
        while org:
            info = format(org)
            with open(filename_chg, 'a') as f:
                f.write(info+'\n')
            org = fobj.readline()

if __name__ == '__main__':
    #print(format(org))
    format_log('/data/user/nginx_log/gen.log', 'stard.log')

#!/usr/bin/python
# coding=utf-8

"""
formatter将多个日志版本,或者来源不同的记录,统一转换为标准日志
比如,此时的日志记录,是由nginx的记录+我们自定义的日志格式的混合物
现转换为统一以我们自己定义的标准格式:
时间/IP/Device/MAC/USER/APP/VER/ACT/Object
格式化器不止一个,对每种情况可以定义,但基本原则是不修改原始信息,其与原始日志是等价的,只是更规整,更容易存放
"""

import datetime
import random
import time
import sys
sys.path.append("..")

from defines import *

"""
if len(sys.argv) != 2:
    print "need 2 parameters: input.log output.log"
    exit()
"""


def getIP():
    index = random.randint(0, len(ips) - 1)
    ip = ips.keys()[index]
    return ip


def getTime():
    dateindex = random.randint(0, len(dates) - 1)
    hours = random.randint(0, 23)
    mins = random.randint(0, 59)
    seconds = random.randint(0, 59)
    stime = dates[dateindex] + ":" + str(hours) + ":" + str(mins) + ":" + str(seconds)
    print stime
    dtime = datetime.datetime.strptime(stime, "%Y/%m/%d:%H:%M:%S")
    dtime = time.mktime(dtime.timetuple())
    dtime = int(dtime)
    return dtime


def format(line=""):
    segs = line.split('[')
    useragent = segs[1].replace(']', '')
    # ip = segs[2].replace(']', '')
    ip = getIP()
    # dtime = segs[2].split()[0]
    # dtime = datetime.datetime.strptime(dtime, "%d/%b/%Y:%H:%M:%S")
    # dtime = time.mktime(dtime.timetuple())
    # dtime = int(dtime)
    dtime = getTime()
    log = segs[4].replace(']', '')
    logs = log.split("/")
    # 时间/IP/Device/MAC/USER/APP/VER/ACT/Object
    r = {
        'useragent': useragent,
        'dtime': dtime,
        'ip': ip,
        'device': logs[4],
        'mac': logs[3],
        'user': logs[2],
        'app': logs[5],
        'ver': logs[6],
        'act': logs[7],
        'content': logs[8]
    }

    res = "%s/%s/%s/%s/%s/%s/%s/%s/%s" % (
        r['dtime'], r['ip'], r['device'], r['mac'], r['user'], r['app'], r['ver'], r['act'], r['content'])
    return res


of = file("../data/standard/std_user_behavior.log", "w")

for line in file("../data/original/user_behavior.log", "r"):
    of.write(format(line) + "\n")

of.close()

# print getTime()

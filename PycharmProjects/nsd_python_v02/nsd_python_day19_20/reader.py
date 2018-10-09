#!/usr/bin/env python3
#--*--coding: utf8--*--
import time

f = open('stard.log', 'r')

def GetDate(timeStamp=1):
    timeArray = time.localtime(float(timeStamp))
    sdate = time.strftime("%Y-%m-%d", timeArray)
    shour = time.strftime("%H", timeArray)
    smin = time.strftime("%M", timeArray)
    return [sdate, shour, smin]

def read():
    line = f.readline().strip('\n')
    #print(line)
    seg = line.split('/')
    #print(seg)
    if len(seg) < 8:
        return None
    [sdate, shour, smin] = GetDate(seg[0])

    res = {
        "sdate": sdate,
        "shour": shour,
        "smin": smin,
        "ip": seg[1],
        "dev": seg[2],
        "mac": seg[3],
        "user": seg[4],
        "app": seg[5],
        "ver": seg[6],
        "act": seg[7],
        "content": seg[8]
    }
   # print(res)
    return res



if __name__ == '__main__':
    read()
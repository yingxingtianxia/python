#！/usr/bin/env python3
#--*--coding: utf8--*--
import wmi

c = wmi.WMI()
def getMemInfo():
    for mem in c.Win32_PhysicalMemory():
        ret0 = mem.SerialNumber
        print(ret0)

getMemInfo()
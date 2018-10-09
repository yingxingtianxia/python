#!/usr/bin/env python
#--coding: utf8--
x = int(raw_input('请输入第一个数：'))
y = int(raw_input('请输入第二个数：'))
Max = max(x, y)
Min = min(x, y)
z = int(raw_input('请输入第三个数：'))
if z > Max:
    print '%s < %s < %s' % (Min, Max, z)
elif z < Min:
    print '%s < %s < %s' % (z, Min, Max)
else:
    print '%s < %s < %s' % (Min, z, Max)
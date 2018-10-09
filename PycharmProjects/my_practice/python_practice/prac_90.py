#!/usr/bin/env python
#--coding: utf8--
#list
#新建列表
testList = [10086, '中国移动', [1,2,3,4]]
#访问列表长度
print len(testList)
#到列表结尾
print testList[1:]
#向列表中添加元素
testList.append('I\'m new here')

print len(testList)
print testList[-1]
print testList.pop(1)
print len(testList)
print testList
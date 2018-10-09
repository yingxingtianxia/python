#!/usr/bin/env python3
#--*--coding: utf8--*--
str1 = 'abc'
#将str类型转换成bytes类型，需要指定str编码
bstr1 = bytes(str1, encoding='utf8')
print(bstr1)

#将收到的bytes类型转成utf8字符串
str2 = str(bstr1, encoding='utf8')
print(str2)

#!/usr/bin/env python
#--coding: utf8--
#深拷贝和浅拷贝
import copy

a_list = [1, 2, 3]
b_list = ['a', 'b', a_list]

c_list = copy.copy(b_list)
d_list = copy.deepcopy(b_list)

print '浅拷贝是%s: ' % c_list
print '深拷贝是%s: ' % d_list
a_list[0] = 4
print a_list
print '更新后浅拷贝是%s: ' % c_list
print '更新后深拷贝是%s: ' % d_list

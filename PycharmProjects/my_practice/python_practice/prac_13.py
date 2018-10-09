#!/usr/bin/env python
#--coding: utf8--
# for num in range(100, 1000):
#     num_str = str(num)
#     x = int(num_str[0])
#     y = int(num_str[1])
#     z = int(num_str[2])
#     if num == x ** 3 + y ** 3 + z ** 3:
#         print num

for i in range(100, 1000):
    if i == int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3:
        print i
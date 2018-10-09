#!/usr/bin/env python3
#--*--coding: utf8--*--
fiber = [0, 1]
for i in range(2,10):
    new_num = fiber[i-2] + fiber[i-1]
    fiber.append(new_num)

print(fiber)
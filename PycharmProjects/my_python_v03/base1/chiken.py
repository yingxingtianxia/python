#!/usr/bin/env python3
#--*--coding: utf8--*--
#共有100元，买100只鸡，公鸡5元，母鸡3元，小鸡1元3只，
#求各类能买多少
import time

start = time.time()

for x in range(21):
    for y in range(34):
        for z in range(3, 101, 3):
            if x+y+z == 100 and 5*x+3*y+z/3 == 100:
                print(x, y, z)

end = time.time()
running_time = end -start
print(running_time)
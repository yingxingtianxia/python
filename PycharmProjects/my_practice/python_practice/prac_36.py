#!/usr/bin/env python
#--coding: utf8--
def sushu(num=100):
    result = []
    if num == 1:
        result.append(num)
    else:
        for i in range(2, num+1):
            k = i/2+1
            for j in range(2, k):
                if i%j == 0:
                    break
            else:
                result.append(i)

    return result

if __name__ == '__main__':
    print sushu()
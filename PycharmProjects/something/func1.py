#!/usr/bin/env python3
def chengfabiao(n=9):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("%s X %s = %s\t" % (j, i, i*j),end='')
        print()

if __name__ == '__main__':
    chengfabiao(5)
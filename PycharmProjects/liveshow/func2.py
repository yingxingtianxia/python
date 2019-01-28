#!/usr/bin/env python3
def foo(arg,*args,**kwargs):
    print(arg,args,kwargs)


if __name__ == '__main__':
    foo(1,2,3,4, 5,a=1,b=2,c=3)
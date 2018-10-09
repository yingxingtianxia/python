#!/usr/bin/env python
#--coding: utf8--
def main():
    num =int(raw_input('请输入一个数字：'))
    print num , '=',
    while num != 1:
        for i in range(2, num+1):
            if num % i == 0:
                num /= i
                if num == 1:
                    print '%s' %  i
                else:
                    print '%s *' % i,

if __name__ == '__main__':
    main()

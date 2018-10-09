#!/usr/bin/env python3
#--*--coding: utf8--*--
fobj = open('hello.txt', 'a')
fobj.write('hello world!\n')
fobj.flush()
fobj.writelines(['line2\n', 'line3\n'])
fobj.close()
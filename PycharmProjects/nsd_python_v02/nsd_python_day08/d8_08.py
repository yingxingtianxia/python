#!/usr/bin/env python
#--coding: utf8--
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):                          #外部返回
        return self.title

#    def __repr__(self):                         #内部返回
#        return self.title

    def __call__(self):
        print '%s is written by %s' % (self.title, self.author)

if __name__ == '__main__':
    py_book = Book('Core Python', 'Wesley')
    print py_book
    py_book()
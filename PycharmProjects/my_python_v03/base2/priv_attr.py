#!/usr/bin/env python3
#--*--coding: utf8--*--
class Book():
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.pages = pages

    def __str__(self):
        return '<%s>' % self.__title


if __name__ == '__main__':
    b1 = Book('Core Python', 'welsily', 800)
    print(b1)
    print(b1.pages)
    print(b1._Book__title)
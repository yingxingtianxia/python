#!/usr/bin/env python3
#--*--coding: utf8--*--
class Cart_Box():
    box = []
    def add(self, pcount):
        self.box.append(pcount)
        print(self.box)
    def size(self):
        return len(self.box)
    def counts(self):
        sumQ = 0
        for i in self.box:
            sumQ += int(i)

        return sumQ
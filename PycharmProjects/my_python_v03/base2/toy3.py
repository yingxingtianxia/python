#!/usr/bin/env python3
#--*--coding: utf8--*--
class BearToy():
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def sing(self, song):
        print(song)


class NewBearToy(BearToy):
    def __init__(self, size, color, material):
        #BearToy.__init__(self, size, color)
        super(NewBearToy, self).__init__(size, color)
        self.material = material

    def run(self):
        print('I can run')


if __name__ == '__main__':
    b1 = NewBearToy('middle', 'brown', 'fur')
    print(b1.size)
    b1.run()
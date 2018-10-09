#!/usr/bin/env python3
# --*--coding: utf8--*--
import time
import threading

nums = [4, 2]


class ThreadFunc():
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop %d at %s' % (nloop, time.ctime()))
    time.sleep(nsec)
    print('loop %d done at %s' % (nloop, time.ctime()))


def main():
    print('starting at: %s' % time.ctime())
    threads = []
    for i in range(2):
        t = threading.Thread(target=ThreadFunc(loop, (i, nums[i]), loop.__name__))
        threads.append(t)
    for i in range(2):
        threads[i].start()
    for i in range(2):
        threads[i].join()
    print('all done at %s' % time.ctime())


if __name__ == '__main__':
    main()

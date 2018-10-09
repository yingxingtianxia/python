#!/usr/bin/env python3
#--*--coding: utf8--*--
import threading
import time

nums = [4, 2]

def loop(nloop, nsec):
    print('start loop %d, at %s' %(nloop, time.ctime()))
    time.sleep(nsec)
    print('loop %d done at %s' % (nloop, time.ctime()))

def main():
    print('starting at: %s' % time.ctime())
    threads = []
    for i in range(2):
        t = threading.Thread(target=loop, args=(i, nums[i]))
        threads.append(t)
    #print(threads)
    for i in range(2):
        threads[i].start()

    for i in range(2):
        threads[i].join()
    print('all done at %s' % time.ctime())

if __name__ == '__main__':
    main()
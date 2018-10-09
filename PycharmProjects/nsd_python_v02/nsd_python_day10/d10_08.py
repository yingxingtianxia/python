#!/usr/bin/env python
#--coding: utf8--
import threading
import time

nums = [4,2]

def loop(nloop, nsec):
    print 'Start loop %d, at %s' % (nloop, time.ctime())
    time.sleep(nsec)
    print 'Loop %d done at %s' % (nloop, time.ctime())

def main():
    print 'Starting at: %s' % time.ctime()
    threads = []
    for i in range(2):
        t = threading.Thread(target=loop, args=(i, nums[i]))
        threads.append(t)

    for i in range(2):
        threads[i].start()

    for i in range(2):
        threads[i].join()

    print 'all Done at: %s' % time.ctime()

if __name__ == '__main__':
    main()
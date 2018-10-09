#!/usr/bin/env python
#--coding: utf8--
import time
import random

play_it = raw_input('do you want to play it.(\'y\' or \'n\')')
while play_it == 'y':
    c = raw_input('input a character:\n')
    i = random.randint(0,2**32) % 100
    print 'please input number you guess:\n'

    start = time.clock()
    a = time.time()
    guess = int(raw_input('input your guess:\n'))

    while guess != i:
        if guess > i:
            print 'please input a smaller number'
            guess = int(raw_input('input your guess:\n'))
        else:
            print 'please input a larger number'
            guess = int(raw_input('input your guess:\n'))

    end = time.clock()
    b = time.time()
    var = (end - start) /18.2

    #print 'it took you %6.3 seconds' % time.difftime(b,a)

    if var < 15:
        print 'you are clever'
    elif var < 25:
        print 'you are normal'
    else:
        print 'you are stupid'

    print 'Congradulations'
    print 'the number you guess is %d' % i
    play_it = raw_input('do you want to play it.')
#！/usr/bin/env python3
#--*--coding: utf8--*--
from random import randint, choice
import sys

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def chuti():
    cmds = {'+':add, '-':sub}
    numbers = [randint(1,50) for i in range(2)]
    numbers.sort(reverse=True)
    op = choice('+-')
    result = cmds[op](*numbers)
    prompt = '%s %s %s = ' % (numbers[0], op, numbers[1])

    for i in range(3):
        try:
            answer = int(input(prompt))
        except ValueError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\nBye')
            sys.exit()

        if answer == result:
            print('Good')
            break
        else:
            print('Wrong')
    else:
        print('%s%s' % (prompt,result))

def main():
    while True:
        chuti()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\nBye')
            yn = 'n'
        if yn == 'n':
            break

if __name__ == '__main__':
    main()
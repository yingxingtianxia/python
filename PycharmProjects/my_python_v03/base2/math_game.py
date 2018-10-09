#!/usr/bin/env python3
#--*--coding: utf8--*--
import random

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-':sub}
    nums  = [random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op = random.choice('+-')
    result = cmds[op](*nums)
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])

    # for i in range(3):
    #     try:
    #         answer = int(input(prompt))
    #     except:
    #         continue
    #
    #     if answer == result:
    #         print('回答正确')
    #         break
    #     else:
    #         print('回答错误')
    # else:
    #     print('%s%s' % (prompt, result))

    tries = 0
    while tries < 3:
        try:
            answer = int(input(prompt))
        except:
            continue

        if answer == result:
            print('回答正确')
        else:
            print('回答错误')
            tries += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while True:
        exam()
        try:
            go_on = input('是否继续(y/n)：').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            go_on = 'n'
        if go_on in 'Nn':
            print('\n拜拜')
            break


if __name__ == '__main__':
    main()
#！/usr/bin/env python3
#--*--coding: utf8--*--
import random, sys

all_choice = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]

prompt = """(0) 石头
(1) 剪刀
(2) 布
Please input your choice(0/1/2): """

pwin = 0
cwin = 0

while pwin < 2 and cwin < 2:
    computer = random.choice(all_choice)
    try:
        ind = int(input(prompt))
        player = all_choice[ind]
    except (ValueError, IndexError):
        print('Invalid input. Try again')
        continue
    except (KeyboardInterrupt, EOFError):
        print('\nBye')
        sys.exit()

    print('Your choice:', player, "Computer's choice:", computer)
    if player == computer:
        print('平局')
    elif [player, computer] in win_list:
        pwin += 1
        print("You win")
    else:
        cwin += 1
        print("You lose")
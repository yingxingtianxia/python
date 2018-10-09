#!/usr/bin/env python3
#--*--coding: utf8--*--
import sys

stack = []

def push_it():
    item = input('压栈数据：')
    stack.append(item)

    return stack

def pop_it():
    stack.pop()

    return stack

def view_it():
    print(stack)

def show_menu():
    prompt = """请做出如下选择：
【0】：压栈
【1】：出栈
【2】：查询
【3】：退出
请在（0/1/2/3）中选择："""
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('输入必须在（0/1/2/3）中选择')
            continue

        if choice == '3':
            sys.exit()

        cmds[choice]()

        # elif choice == '3':
        #     sys.exit()
        # elif choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # elif choice == '2':
        #     view_it()




if __name__ == '__main__':
    show_menu()
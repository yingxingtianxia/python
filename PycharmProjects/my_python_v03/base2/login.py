#!/usr/bin/env python3
#--*--coding: utf8--*--
import getpass

userdb = {}

def register():
    username = input('请输入用户名：')
    if username in userdb:
        print('用户已经存在')
    else:
        password = getpass.getpass('请输入密码：')
        userdb[username] = password

def login():
    username = input('请输入用户名：')
    password = getpass.getpass('请输入密码：')
    #if username not in userdb or userdb[username] != password:
    if userdb.get(username) != password:
        print('登陆失败')
    else:
        print('登陆成功')

def show_menu():
    prompt = """【0】：注册
【1】：登陆
【2】：退出
请做出选择（0/1/2）："""
    cmds = {'0': register, '1': login}
    while True:
        choice = input(prompt).rstrip()[0]
        if choice not in '012':
            print('输入无效')
            continue
        if choice == '2':
            break

        cmds[choice]()


if __name__ == '__main__':
    show_menu()
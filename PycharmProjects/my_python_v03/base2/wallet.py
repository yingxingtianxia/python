#!/usr/bin/env python3
#日期     开销     收入    余额    备注

import time
import pickle as p
import os


def spend_money(record, wallet):
    date = time.strftime('%Y-%m-%d')
    amount = int(input('金额：'))
    comment = input('备注：')
    with open(wallet, 'wb') as fobj:
        balance = p.load(fobj) - amount
    with open(wallet, 'wb') as fobj:
        p.dump(balance, fobj)

    with open(record, 'a') as fobj:
        fobj.write(
            '%-15s%-8s%-8s%-10s%-20s\n' %
            (date, amount, 'n/a', balance, comment)
        )


def save_money(record, wallet):
    date = time.strftime('%Y-%m-%d')
    amount = int(input('金额：'))
    comment = input('备注：')
    with open(wallet, 'wb') as fobj:
        balance = p.load(fobj) + amount
    with open(wallet, 'wb') as fobj:
        p.dump(balance, fobj)

    with open(record, 'a') as fobj:
        fobj.write(
            '%-15s%-8s%-8s%-10s%-20s' %
            (date, 'n/a', amount, balance, comment)
        )

def query(record, wallet):
    with open(record) as fobj:
        for line in fobj:
            print(line, end='')

    with open(wallet) as fobj:
        balance = p.load(fobj)

    print('当前余额：%s' % balance)


def show_menu():
    prompt = """【0】记录开销
【1】记录收入
【2】查询记录
【3】退出
请选择（0/1/2/3）："""
    cmds = {'0': spend_money, '1': save_money, '2': query}
    record = 'record.txt'
    wallet = 'wallet.data'

    if not os.path.exists(wallet):
        with open(wallet, 'wb') as fobj:
            p.dump(10000, fobj)


    while True:
        try:
            choice = input(prompt).rstrip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\n拜拜')
            choice = '3'
        if choice not in '0123':
            print('输入无效，请重新输入')
            continue

        if choice == '3':
            break

        cmds[choice](record, wallet)


if __name__ == '__main__':
    show_menu()
#!/usr/bin/env python3
# -*-coding: utf8-*-

# 记账簿

import os
import pickle as p
import time

def save_money(wallet_file, record_file):
    amount = int(input("amount: "))  #数额
    comment = input("comment: ")     #备注
    date = time.strftime("%Y-%m-%d") #时间

    with open(wallet_file) as fobj:
        balance = p.load(fobj) + amount
    with open(wallet_file, 'w') as fobj:
        p.dump(balance, fobj)
    with open(record_file, 'a') as fobj:
        fobj.write(
            "%-12s%-8s%-8s%-10s%-20s\n" % \
            (date, amount, 'n\a', balance, comment)
        )


def cost_money(wallet_file, record_file):
    amount = int(input("amount: "))  # 数额
    comment = input("comment: ")  # 备注
    date = time.strftime("%Y-%m-%d")  # 时间

    with open(wallet_file) as fobj:
        balance = p.load(fobj) - amount
    with open(wallet_file, 'w') as fobj:
        p.dump(balance, fobj)
    with open(record_file, 'a') as fobj:
        fobj.write(
            "%-12s%-8s%-8s%-10s%-20s\n" % \
            (date,  'n\a', amount, balance, comment)
        )

def query(wallet_file, record_file):
    print("%-12s%-8s%-8s%-10s%-20s\n" % \
        ('date',  'save', 'amount', 'balance', 'comment'))
    with open(record_file) as fobj:
        for line in fobj:
            print(line),
    with open(wallet_file) as fobj:
        print("New Balance: \033[31;1m%s\033[0m" % p.load(fobj))




def main():
    cmds = {'0': save_money, '1': cost_money, '2': query}
    wallet_file = 'wallet.data'
    record_file = 'record.txt'
    prompt = """(0)save money
(1)cost money
(2)query history
(3)quit
Please input your choice(0/1/2/3):"""
    if not os.path.exists(wallet_file):  #判断文件是否存在
        with open(wallet_file, 'w') as fobj:
            p.dump(10000, fobj)
    if not os.path.exists(record_file):
        os.mknod(record_file)
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid choice. Try again.')
            continue

        if choice == '3':
            break

        cmds[choice](wallet_file, record_file)


if __name__ == '__main__':
    main()
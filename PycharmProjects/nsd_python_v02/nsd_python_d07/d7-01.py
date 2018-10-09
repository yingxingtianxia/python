#！/usr/bin/env python3
#--*--coding: utf8--*--
import os
import pickle as p
import time

def save_money(wallet_file, record_file):
    amount = int(input('amount: '))
    comment = input('comount: ')
    date = time.strftime('%Y-%m-%d')

    with open(wallet_file) as fobj:
        balance = p.load(fobj) + amount
    with open(wallet_file, 'w') as fobj:
        p.dump(balance, fobj)
    with open(record_file, 'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s\n' % \
            (date, amount, 'n/a', balance, comment)
        )

def cost_money(wallet_file, record_file):
    amount = int(input('amount: '))
    comment = input('comount: ')
    date = time.strftime('%Y-%m-%d')

    with open(wallet_file) as fobj:
        balance = p.load(fobj) - amount
    with open(wallet_file, 'w') as fobj:
        p.dump(balance, fobj)
    with open(record_file, 'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s\n' % \
            (date, 'n/a', amount, balance, comment)
        )

def query(wallet_file, record_file):
    print('%-12s%-8s%-8s%-10s%-20s\n' % \
            ('date', 'save', 'amount', 'balance', 'comment'))
    with open(record_file) as fobj:
        for line in fobj:
            print(line)
    with open(wallet_file) as fobj:
        print('New balance:', p.load(fobj))

def main():
    cmds = {'0': save_money, '1': cost_money, '2': query}
    wallet_file = 'wallet.txt'
    record_file = 'record.txt'
    if not os.path.exists(wallet_file):
        with open(wallet_file, 'w') as fobj:
            p.dump('10000', fobj)
    if not os.path.exists(record_file):
        open(record_file, 'a')
    prompt = """(0): save_money
(1): cost_money
(2): query_money
(3): quit
Please input your choice(0/1/2/3)"""
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid choice, do again.')
            continue

        if choice == '3':
            break

        cmds[choice](wallet_file, record_file)

if __name__ == '__main__':
    main()
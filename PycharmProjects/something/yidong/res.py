import xlrd
import sys
import os
import time

def get_yd(yd_table,direction):
    #获取两个工作表
    data = xlrd.open_workbook(yd_table)
    tables = data.sheets()
    # print(tables)

    #处理退学表
    tx = []
    tx_table = tables[0]

    tx_name = tx_table.name
    tx_nrows = tx_table.nrows
    tx_values = tx_table.row_values

    for i in range(1, tx_nrows):
        tx_r_value = tx_values(i)
        if tx_r_value[0] == direction:
            name = tx_r_value[1]
            account = tx_r_value[2].strip('@qq.com')
            tx.append([name,account])
    # print(len(tx))

    #处理转脱产表
    tc = []
    tc_table = tables[1]

    tc_name = tc_table.name
    tc_nrows = tc_table.nrows
    tc_values = tc_table.row_values

    for i in range(1, tc_nrows):
        tc_r_value = tc_values(i)
        if tc_r_value[0] == direction:
            name = tc_r_value[1]
            account = tc_r_value[2]
            tc.append([name,account])
    # print(len(tc))

    yd_dic = {"退学":tx, "转脱产":tc}

    return yd_dic

#获取当前群成员列表
def get_mems(mem_table):
    data = xlrd.open_workbook(mem_table)
    tables = data.sheets()
    mem_dic = {}

    for i in range(len(tables)):
        table = tables[i]
        t_name = table.name
        t_nrows = table.nrows
        t_values = table.row_values

        mems = []
        for j in range(1, t_nrows):
            r_value = t_values(j)
            try:
                account = int(r_value[0])
            except ValueError:
                continue
            mems.append(account)

        mem_dic[t_name] = mems

    # pprint.pprint(mem_dic)
    return mem_dic

#计算结果
def grep(yd_dic,mem_dic,direction):
    # print(yd_dic)
    # print(mem_dic)
    #获取在群成员总表

    #查找退学学员
    tx = yd_dic['退学']
    print('本周\033[32m[%s]\033[0m方向\033[32;41m[退学]\033[0m共\033[31m[%s]\033[0m人' % (direction,len(tx)))

    if len(tx) != 0:
        tx_in = []
        for i in tx:
            tx_name = i[0]
            tx_acc = i[1].strip('@qq.com')
            for key in mem_dic.keys():
                for value in mem_dic[key]:
                    if tx_acc == str(value):
                        tx_in.append(tx_acc)
                        print('学员\033[33m[%s]\033[0m\t账号\033[31m[%s]\033[0m\t\t在\033[32m[%s]\033[0m群' % (tx_name,tx_acc,key))

        if len(tx_in) == 0:
            print('\033[32m本周退学表格内学员均不在群\033[0m')

    #查找转脱产学员
    tc = yd_dic['转脱产']
    print('本周\033[32m[%s]\033[0m方向\033[32;41m[转脱产]\033[0m共\033[31m[%s]\033[0m人' % (direction, len(tc)))

    if len(tc) != 0:
        tc_in = []
        for i in tc:
            tc_name = i[0]
            tc_acc = i[1].strip('@qq.com')
            for key in mem_dic.keys():
                for value in mem_dic[key]:
                    if tc_acc == str(value):
                        tc_in.append(tc_acc)
                        print("学员\033[33m[%s]\033[0m\t账号\033[31m[%s]\033[0m\t\t在\033[32m[%s]\033[0m群" % (tc_name,tc_acc,key))

        if len(tc_in) == 0:
            print('\033[32m本周转脱产表格中学员均不在群\033[0m')


if __name__ == '__main__':
    prompt = """本程序根据异动学员表筛选异动且以在群的学员，请保持移动学员表格格式不变
异动表格内部格式为：[
\033[31m[退学]\033[0m学员表为第\033[31m[1]\033[0m张工作表
\033[31m[转脱产]\033[0m学员表为第\033[31m[2]\033[0m张工作表
]
如果不确定请按\033[34;41m[q]\033[0m退出检查
按其他\033[32;43m[任意键]\033[0m进入筛选程序"""
    print(prompt)

    while True:
        try:
            entry = input('请选择（\033[31m[q]\033[0m退出,\033[32m[任意键]\033[0m继续）：')
        except (KeyboardInterrupt,EOFError):
            print('\n\033[31;40m[退出程序]\033[0m')
            sys.exit(1)
        if entry == 'q':
            print('\033[31;40m[退出程序]\033[0m')
            sys.exit(1)
        else:
            print('\033[31;42m[进入筛选程序]\033[0m')

            while True:
                try:
                    yd_table = input('请输入异动学员表名：')
                except (KeyboardInterrupt,EOFError):
                    print('\n\033[31;40m[退出程序]\033[0m')
                    sys.exit(1)
                if not os.path.exists(yd_table):
                    print('当前输入异动学员表名不存在，请核对文件路径名称后重新输入')
                    continue
                else:
                    break

            while True:
                try:
                    mem_table = input("请输入群成员表名：")
                except (KeyboardInterrupt,EOFError):
                    print('\n\033[31;40m[退出程序]\033[0m')
                    sys.exit(1)
                if not os.path.exists(mem_table):
                    print('当前输入群成员表名有误，请核对文件路径名称后重新输入')
                    continue
                else:
                    break

            dirs = ['ACC', 'AID', 'BIG', 'BVD', 'CAD', 'CGB', 'CID', 'CSD', 'ECD', 'EME', 'ESD',
                    'GCA', 'GEM', 'GSD', 'HRM', 'ISD', 'MSD', 'NSD', 'NTD', 'PSD', 'SD', 'TSD',
                    'U3D', 'UCD', 'UED', 'UID', 'VFX', 'VRD', 'WEB']

            while True:
                try:
                    direction = input('请输入需要筛选的方向名：').upper()
                except (KeyboardInterrupt,EOFError):
                    print('\n\033[31;40m[退出程序]\033[0m')
                    sys.exit(1)
                if direction not in dirs:
                    print('当前输入方向名有误，请重新输入')
                    continue
                else:
                    break


            print('所需文件均已输入，请稍候，开始筛选...')
            yd_dic = get_yd(yd_table,direction)
            mem_dic = get_mems(mem_table)
            grep(yd_dic,mem_dic,direction)

            time.sleep(5)

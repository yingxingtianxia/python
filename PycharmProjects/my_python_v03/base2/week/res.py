#!/usr/bin/env python3
#--*--coding: utf8--*--
import xlrd
import sys
import os
#将群成员从excel中取出，做成以群名为key，群成员为value的字典
def qun_member(member_list):
    data = xlrd.open_workbook(member_list)
    tables = data.sheets()
    table_dic = {}
    for i in range(len(tables)):
        table = tables[i]
        nrows = table.nrows
        #print('%s表有%s行' % (table.name, nrows))
        each_table_list = []
        for i in range(nrows):
            value = str(table.row_values(i)).lstrip('[').rstrip(']').rstrip('.0')
            each_table_list.append(value)
        table_dic[table.name] = each_table_list

    return table_dic


#将总表中的三列数据取出，每行数据作为列表的元素做成一个总人数的大列表
def total_list(total_list):
    data = xlrd.open_workbook(total_list)
    table = data.sheets()[0]
    nrows = table.nrows
    total_mem_list = []
    for i in range(1, nrows):
        value = table.row_values(i)
        value = [value[0], str(value[1]).rstrip('.0'), value[2]]
        total_mem_list.append(value)

    return total_mem_list


#在总人数列表中把对应方向的元素过滤出来，组成一个新的只有一个方向的列表
def direct_list(total_mem_list, direction):
    direct_mem_list = []
    for item in total_mem_list:
        if direction.upper() in item:
            direct_mem_list.append(item)

    return direct_mem_list


#把群字典中的值取出来，到单独方向的列表中去过滤有数据的元素，将群名，有效数据的元素组成字典
def filt_direct(qun_dic, direct_mem_list):
    exist_data_dic = {}
    for key in qun_dic.keys():
        exist_data_list = []
        for member in qun_dic[key]:
            for item in direct_mem_list:
                if member in item:
                    exist_data_list.append(item)
                    continue
        exist_data_dic[key] = exist_data_list

    return exist_data_dic


#计算，把有效数据的字典的值进行遍历，列表第三项数值求和，然后除以有效数据列表的长度
#定义一个空列表，把群名，计算结果，有效数据人数以列表的形式存储到空列表中
def count(exist_data_dic):
    res_list = []
    for key in exist_data_dic.keys():
        result = 0
        exist_data_list = exist_data_dic[key]
        for item in exist_data_list:
            try:
                result += item[2]
            except TypeError:
                continue
        res = result / len(exist_data_list) * 100
        res_list.append([key, res, len(exist_data_list)])

    return res_list


#将所有之前定义的函数综合起来，避免主程序过于臃肿
def out_put(member_file, total_file, direction):
    qun_dic = qun_member(member_file)
    total_mem_list = total_list(total_file)
    direct_mem_list = (direct_list(total_mem_list, direction))
    exist_data_dic = filt_direct(qun_dic, direct_mem_list)
    res_list = count(exist_data_dic)

    return res_list


if __name__ == '__main__':
    #out_put函数返回结果是列表，对列表进行遍历，格式化输出结果
    try:
        member_file = input('请输入群成员表格名称：')
    except (KeyboardInterrupt, EOFError):
        print('结束程序')
        sys.exit()
    if not os.path.exists(member_file):
        print('文件不存在，请检查')
        sys.exit()

    try:
        total_file = input('请输入达到率表格名称：')
    except (KeyboardInterrupt, EOFError):
        print('结束程序')
        sys.exit()
    if not os.path.exists(total_file):
        print('文件不存在，请检查')

    try:
        direction = input('请输入方向简写：')
    except (KeyboardInterrupt, EOFError):
        print('结束程序')
        sys.exit()


    result_list = (out_put(member_file, total_file, direction))
    for item in result_list:
        print('%s群的达到率是%.2f%%,活跃人数是%s' % (item[0], item[1], item[2]))

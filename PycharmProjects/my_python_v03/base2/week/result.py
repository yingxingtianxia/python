#!/usr/bin/env python3
#--*--coding: utf8--*--
import os
import xlrd

def transformat(tablename, txtname):
    data = xlrd.open_workbook(tablename)
    table = data.sheets()[0]
    nrows = table.nrows
    with open(txtname, 'a') as fobj:
        for i in range(nrows):
            item = table.row_values(i)
            it = str(item[1]).rstrip('.0')
            item = "%s\t%s\t%s" % (item[0], it, item[2])
            fobj.writelines(item)
            fobj.writelines('\n')


def fangxiang(t_file, fangxiang):
    with open(t_file, 'r') as t_fobj:
        t_fx_list = []
        for line in t_fobj:
            if fangxiang in line:
                line = line.rstrip('\n').split('\t')
                t_fx_list.append(line)

    return t_fx_list


def shaixuan(qun_file, t_list):
    with open(qun_file, 'r') as qun_fobj:
        f_qun = []
        qq_list = qun_fobj.readlines()
        for qq in qq_list:
            qq = qq.rstrip('\n')
            for item in t_list:
                if qq in item:
                    f_qun.append(item)
    return f_qun

def count(qun_file, f_qun):
    qun_name = qun_file.split('/')[1].rstrip('.txt')
    res = 0
    for item in f_qun:
        ma = float(item[2])
        res += ma

    result = res / len(f_qun) * 100
    return '%s群的达到率是%.2f, 活跃人数是%s' % (qun_name, result, len(f_qun))

def out(basedir, zongbiao, txtname, fxm):
    transformat(zongbiao, txtname)
    result = []
    qun_list = list(os.walk(basedir))
    for path, folders, files in qun_list:
        for file in files:
            filename = os.path.join(path, file)
            t_fx_list = fangxiang(txtname, fxm.upper())
            f_qun = shaixuan(filename, t_fx_list)
            res = (count(filename, f_qun))
            result.append(res)

    os.remove(txtname)
    return result


if __name__ == '__main__':
    result = out('base', 'ddl.xlsx','to.txt', 'nsd')
    for item in result:
        print(item)

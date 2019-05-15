import pymysql
import xlrd
import subprocess
import os
import sys
import time

#退出码1    →   数据库创建失败
#退出码2    →   选择时退出程序
#退出码3    →   正常选择退出程序
#退出码4    →   输入总表名时退出程序
#退出码5    →   输入群成员列表名退出程序
#退出码6    →   输入方向名时退出程序

#检测weekdb数据库是否存在，如果存在则打印
def create_db():
    (status,stdout) = subprocess.getstatusoutput(
        'mysql -h127.0.0.1 -P3306 -uroot -p123456 -e "create database if not exists weekdb default character set utf8;"'
    )

    if status:
        print("weekdb数据库创建失败，请登录数据库检查")
        sys.exit(1)
    else:
        print("weekdb数据库已经创建成功")

#获取方向学员QQ与达到率组成列表
def get_total(total_table, direction):
    data = xlrd.open_workbook(total_table)
    tables = data.sheets()
    # print(tables)
    for i in range(len(tables)):
        table = tables[i]
        t_name = table.name
        t_rows = table.nrows
        t_values = table.row_values
        # print('%s you %s hang' % (t_name, t_rows))
        dir_list = []
        for j in range(1, t_rows):
            r_value = t_values(j)
            try:
                r_value[1] = int(r_value[1])
            except ValueError:
                continue
            # print('%s de %s hang shi %s' % (t_name, j, r_value))
            if r_value[0] == direction:
                dir_list.append(r_value)

    return dir_list



#获取群名与群成员QQ号组成字典
def get_qun(members_table):
    data = xlrd.open_workbook(members_table)
    tables = data.sheets()
    qun_dic = {}
    for i in range(len(tables)):
        table = tables[i]
        t_name = table.name
        t_rows = table.nrows
        t_values = table.row_values
        # print('%s %s' % (t_name, t_rows))
        mem_list = []
        for j in range(1, t_rows):
            r_value = int(t_values(j)[0])
            mem_list.append(r_value)
        qun_dic[t_name] = mem_list


    return qun_dic



##数据库操作
#连接数据库
def handle_sql(direction_list, qun_dictory):
    conn = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = '123456',
        db = 'weekdb',
        charset = 'utf8'
    )
    cursor = conn.cursor()


    #重新创建总表
    cursor.execute('drop table if exists total')
    conn.commit()

    cursor.execute('create table total(qq char(15), lv char(10))')

    #将从总excel表中过滤出来的数据写入到weekdb库中的total表
    sql_in_total = 'insert into total values (%s, %s)'
    for i in direction_list:
        # print(i)
        qq = str(i[1])
        lv = str(i[2])
        # print(qq, lv)
        cursor.execute(sql_in_total,(qq,lv))
    conn.commit()

    #创建群成员表，每个群一个表
    for i in qun_dictory.keys():
        cursor.execute('drop table if exists %s' % i)
        conn.commit()
        cursor.execute('create table %s(qq char(15))' % i)
        mems = qun_dictory[i]
        # print(mems)
        #将每个群的群成员写入对应的表
        for mem in mems:
            # print(type(mem))
            cursor.execute('insert into %s values (%s)' % (i, str(mem)))
        conn.commit()
    
    #关闭数据库连接
    cursor.close()
    conn.close()


#查询结果
def query(qun_dictory):
    res_list = []
    for i in qun_dictory.keys():
        stdout = subprocess.getoutput(
            'mysql -h127.0.0.1 -uroot -p123456 -e \
            "select count(lv),avg(lv) from weekdb.total \
            where qq in (select * from weekdb.%s)" | tail -1' % i
        )
        res = stdout.split('\t')
        res.append(i)
        res_list.append(res)

    return res_list

#主函数
def main(total_table,members_table, direction):
    create_db()
    dir_list = get_total(total_table,direction)
    qun_dic = get_qun(members_table)
    handle_sql(dir_list,qun_dic)
    res = query(qun_dic)

    return res

if __name__ == '__main__':
    prompt = """请先确定本机\033[31mMySQL数据库服务\033[0m已经运行
且服务端口号为\033[31m3306\033[0m
数据库用户名\033[31mroot\033[0m
数据库密码\033[31m123456\033[0m可以登录
如不确定请按\033[34;41m[q]\033[0m退出检查
按其他\033[32;43m[任意键]\033[0m进入计算程序"""

    #打印提示信息
    print(prompt)
    
    #进入用户选择
    while True:
        try:
            entry = input("请选择（\033[31m[q]\033[0m退出）：")
        except (KeyboardInterrupt,EOFError):
            print('\n\033[31;40m[退出程序]\033[0m')
            sys.exit(2)
        if entry == 'q':
            print("\033[31;40m[退出程序]\033[0m")
            sys.exit(3)
        else:
            print("\033[31;42m[进入运算程序]\033[0m")

            dirs = ['ACC','AID','BIG','BVD','CAD','CGB','CID','CSD','ECD','EME','ESD',
                    'GCA','GEM','GSD','HRM','ISD','MSD','NSD','NTD','PSD','SD','TSD',
                    'U3D','UCD','UED','UID','VFX','VRD','WEB'
                    ]

            ##进入运算程序
            #判断总表是否正确
            while True:
                try:
                    total_table = input('请输入总表名：')
                except (KeyboardInterrupt,EOFError):
                    print('\n\033[31;40m[退出程序]\033[0m')
                    sys.exit(4)
                if not os.path.exists(total_table):
                    print('当前输入的总表名不存在，请核对路径文件名后重新输入')
                    continue
                else:
                    break
            #判断成员表是否正确
            while True:
                try:
                    members_table = input('请输入群成员列表名：')
                except (KeyboardInterrupt,EOFError):
                    print('\n\033[31;40m[退出程序]\033[0m')
                    sys.exit(5)
                if not os.path.exists(members_table):
                    print('当前输入群成员列表名不存在，请核对路径文件名后重新输入')
                    continue
                else:
                    break
            #判断方向名是否正确
            while True:
                try:
                    direction = input('请输入方向名：').upper()
                except (KeyboardInterrupt,EOFError):
                    print('\n\033[31;40m[退出程序]\033[0m')
                    sys.exit(6)
                if direction not in dirs:
                    print('当前输入方向名有误，请重新输入')
                    continue
                else:
                    break

            #调用运算程序
            print('\033[32m[请稍候，开始进行计算]\033[0m')
            results = main(total_table,members_table,direction)
            #打印计算结果
            if len(results) == 0:
                print('jisuanyouwu')
                sys.exit()
            else:
                print('\033[32m[计算结束，马上打印结果]\033[0m')
                lvs = 0
                for res in results:
                    qun_name = res[2]
                    qun_mems = res[0]
                    try:
                        qun_lv = float(res[1])
                    except ValueError:
                        continue
                    lvs += qun_lv
                    #打印单群计算结果
                    print("\033[31m[%s]\033[0m群有\033[31m[%s]\033[0m名活跃成员，该群的达到率是\033[32m[%.2f%%]\033[0m" % (qun_name,qun_mems,qun_lv*100))

                #打印平均计算结果
                print("本次计算共有\033[31m[%s]\033[0m个群，平均达到率是\033[32m[%.2f%%]\033[0m" % (len(results),lvs*100/len(results)))

            time.sleep(5)

#!/usr/bin/python
# coding=utf-8

import mysql.connector as cn

config = {
    'host': '192.168.99.100',
    'port': 43306,
    'database': 'ecom',
    'user': 'happy',
    'password': 'happy',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
}
db = cn.Connect(**config)
cursor = db.cursor()

def query(sql):
    global config
    try:

        cursor.execute(sql)
        if sql.lower().find("select") == -1:
            db.commit()
            return cursor.rowcount, []
        else:
            rows = cursor.fetchall()
            return len(rows), rows


    except Exception, e:
        print str(e.__class__)+" SQLError:"+str(sql)
        cursor.close()
        db.close()
        return 0, []


def getMaxId(table, field):
    n, rows = query("select max(%s) from %s" % (field, table))
    return rows[0][0]


if __name__ == "__main__":
    #sql="insert into bill value('%s','%s','%s','%s')"%(4,6,13.5,'adfkd')
    sql="select * from product where id=1"
    n,rows=query(sql)
    print rows

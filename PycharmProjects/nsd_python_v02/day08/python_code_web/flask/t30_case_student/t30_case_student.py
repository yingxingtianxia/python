#!/bin/python
# coding=utf8

from flask import Flask, request, redirect, url_for
from flask import render_template
import db.mysql_connector_DB as DB
db = DB.getDB()

import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"




@app.route('/')
@app.route('/list')
def list():
    count, res = db.query('select * from student')
    print res
    return render_template("student/list.htm", data=res)


@app.route('/edit/<id>')
def edit(id):
    print id
    fs = (id, "", "")
    if int(id) != 0:
        fs = db.queryOne('select * from student where id=%s' % id)
    return render_template("student/edit.htm", fs=fs)


@app.route('/save', methods=['GET', 'POST'])
def save():
    id = request.values.get("id")
    xm = request.values.get("xm")
    age = request.values.get("age")
    print "idddd=", id
    if int(id) != 0:
        sql = "update student set xm='%s', age='%s' where id='%s'" % (xm, age, id)
    else:
        row = db.queryOne("select max(id) from student")
        maxid = int(row[0]) + 1
        sql = "insert into student values('%s','%s','%s')" % (maxid, xm, age)
    print sql
    db.query(sql)
    return redirect(url_for("list"))


@app.route('/delraw/<id>')
def delraw(id):
    sql = "delete from student where id=%s" % id
    db.query(sql)
    return list()


if __name__ == '__main__':
    app.run(debug=True)

#!/bin/python
# coding=utf8

from flask import Blueprint, request, render_template, redirect, session

import tools.mysql_connector_DB as DB
db = DB.getDB()

login = Blueprint('login', __name__)


@login.route('/')
def login_view():
    return render_template("login.html", msg="")


@login.route('/login')
def login_check():
    clogin = request.values.get("clogin");
    cpwd = request.values.get("cpwd");
    n, rows = db.query("select * from user where clogin='%s' and cpwd='%s'" % (clogin, cpwd))
    if n == 1:
        session["uid"]=rows[0][0]
        session['clogin']=clogin
        return redirect("/product/list")
    else:
        return render_template("login.html", msg=u"账号或者密码错误")


@login.route('/regist')
def login_regist():
    clogin = request.values.get("clogin");
    cpwd = request.values.get("cpwd");
    cpwd2 = request.values.get("cpwd2");

    if cpwd != cpwd2:
        return render_template("regist.html", msg=u"密码不一致!")

    n, rows = db.query("select * from user where clogin='%s' and cpwd='%s'" % (clogin, cpwd))
    if n == 1 & n > 1:
        return render_template("regist.html", msg=u"登陆名称已经存在,请换个名称!")
    else:
        mid = db.getMaxId("user", "id")
        uid = int(mid) + 1
        sql = "insert INTO user VALUE ('%s','%s','%s','')" % (uid, clogin, cpwd)
        print sql
        db.query(sql)

        return render_template("login.html", msg=u"请登陆")

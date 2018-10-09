#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Blueprint
from flask import render_template
from flask import request
from nsd_python_v02.nsd_python_day18.dbdriver.DB import *
from flask import redirect

blue_regist = Blueprint('blue_regist', __name__)
blue_user_save = Blueprint('blue_user_save', __name__)

@blue_regist.route('/user/regist')
def regist():
    return render_template('regist.html')

@blue_user_save.route('/user/save')
def user_save():
    id = int(request.values.get('id'))
    name = request.values.get('cname')
    pwd = request.values.get('cpwd')

    db = getDB()
    sql = 'insert into user values ("%s", "%s", "%s")' % (id, name, pwd)
    db.query(sql)

    n, rows = db.query("select * from user where cname='%s' and cpwd='%s'" % (name, pwd))
    if n == 1:
        return redirect('/')
    else:
        return redirect('/user/regist')
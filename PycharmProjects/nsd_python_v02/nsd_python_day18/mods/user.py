#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from nsd_python_v02.nsd_python_day18.dbdriver.DB import *

db = getDB()

blue_user = Blueprint('blue_user',__name__)

@blue_user.route('/')
def login():
    second = request.values.get('second')
    if not second:
        msg = ''
        return render_template('login.html', msg=msg)
    else:
        cname = request.values.get('cname')
        cpwd = request.values.get('cpwd')
        sql = 'select * from user where cname="%s" and cpwd="%s"' % (cname, cpwd)
        n, rows = db.query(sql)
        if n == 1:
            return redirect('/product/list')
        else:
            msg = '用户名或密码有误'
            return render_template('login.html', msg = msg)

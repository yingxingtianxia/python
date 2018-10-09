#!/bin/python
# coding=utf8

from flask import Blueprint,render_template,request,redirect,url_for
import tools.mysql_connector_DB as DB

user = Blueprint('user', __name__)
db = DB.getDB()

@user.route('/')
@user.route('/login')
def login():
    return render_template("login.html")

@user.route('/login_check')
def login_check():
    xm=request.values.get("xm")
    pwd=request.values.get("pwd")
    if db_check(xm,pwd):
       #return redirect(url_for("product.product_list"))
       return redirect("/product_list")
    else:
        return render_template("login.html",msg="xm or pwd is wrong!")

@user.route('/test')
def db_check(cname,cpwd):
    sql="select * from user where clogin='%s' and cpwd='%s'"%(cname,cpwd)
    count,rows=db.query(sql);
    if count==1:
        return True
    else:
        return False
    #return count

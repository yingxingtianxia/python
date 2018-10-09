#!/bin/python
# coding=utf8

from flask import Blueprint,render_template,request,redirect,url_for
import tools.mysql_connector_DB as DB

product = Blueprint('proudct', __name__)
db = DB.getDB()

@product.route('/product_list')
def product_list():
    sql="select * from product limit 8"
    count,rows=db.query(sql)
    return render_template("product_list.html",rows=rows)

@product.route('/product_detail/<pid>')
def product_detail(pid):
    sql="select * from product where id='%s'"%pid
    count,rows=db.query(sql)
    return render_template("product_detail.html",row=rows[0])

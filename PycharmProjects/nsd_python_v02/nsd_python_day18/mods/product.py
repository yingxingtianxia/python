#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Blueprint
from flask import render_template
from nsd_python_v02.nsd_python_day18.dbdriver import DB

db = DB.getDB()

blue_product = Blueprint('blue_product', __name__)

@blue_product.route('/product/list', methods=['GET', 'POST'])
def list():
    sql = 'select * from product limit 8'
    n, products = db.query(sql)
    return render_template('product_list.html', pros=products)\

@blue_product.route('/product/detail/<id>', methods=['GET', 'POST'])
def detail(id):
    sql = 'select * from product where id="%s"' % id
    n, product = db.query(sql)
    return render_template('product_detail.html', pros=product)
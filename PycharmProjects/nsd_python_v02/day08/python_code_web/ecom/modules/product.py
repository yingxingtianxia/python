#!/bin/python
# coding=utf8

from flask import Blueprint, render_template, request, session

import tools.mysql_connector_DB as DB
db = DB.getDB()

product = Blueprint('product', __name__)


@product.route('/product/list')
def product_list():
    cols = 4
    n, rows = db.query("select * from product limit 8");
    nrow = int(round(n * 1.0 / cols + 0.49))
    p_list = []
    for i in range(0, nrow):
        row = []
        for j in range(0, cols):
            row.append(rows[i * cols + j])
        p_list.append(row)

    clogin = session["clogin"]
    return render_template("product_list.html", rows=p_list, clogin=clogin)


@product.route('/product/detail')
def product_detail():
    id = request.values.get("pid");
    n, rows = db.query("select * from product where id='%s'" % (id));
    row = rows[0]
    return render_template("product_detail.html", row=row)

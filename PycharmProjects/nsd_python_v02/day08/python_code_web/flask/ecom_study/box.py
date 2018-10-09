#!/bin/python
# coding=utf8

from flask import session,Blueprint,render_template,request,redirect,url_for
import tools.mysql_connector_DB as DB

box = Blueprint('box', __name__)
db = DB.getDB()

@box.route('/box_add')
def box_add():
    pid=request.values.get("pid")
    pid=int(pid)
    mybox=[]
    mybox=session.get("mybox")
    if mybox:
        mybox.append(pid)
    else:
        mybox=[]
        mybox.append(pid)

    session["mybox"]=mybox


    return "box=%s"%mybox

@box.route('/box_list')
def box_list():
    pids=session.get("mybox")
    sql=""
    for id in pids:
        sql=sql+str(id)+","
    sql =sql[:-1]
    sql="select * from product where id in ("+sql+")"
    #return sql
    #print sql;
    #sql="sel"
    count,list=db.query(sql)
    tm=0.0
    for p in list:
        tm=tm+float(p[4])

    return render_template("box_list.html",list=list,total_money=tm)
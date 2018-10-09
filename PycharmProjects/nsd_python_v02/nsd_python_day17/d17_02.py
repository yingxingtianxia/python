#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import nsd_python_v02.nsd_python_day17.DB as DB

app = Flask(__name__)
app.config["SECTET_KEY"] = 'TEST'

@app.route('/')
def data_login():
    return render_template('login.html')

@app.route('/data/show')
def data_show():
    db = DB.getDB()
    sql = "select * from student"
    n, rows = db.query(sql)
    return render_template('show.html', data=rows)

@app.route('/data/add')
def data_add():
    return render_template('add.html')

@app.route('/data/save/add')
def data_save_add():
    db = DB.getDB()
    name = request.values.get('name')
    age = request.values.get('age')

    row = db.queryOne('select max(id) from student')
    id = int(row[0]) + 1

    sql = "insert into student values ('%s', '%s', '%s')" % (id, name, age)
    db.query(sql)
    return redirect('/data/show')

@app.route('/data/cancel/add')
def data_cancel_add():
    return redirect('/data/show')

@app.route('/data/delete')
def data_delete():
    return render_template('delete.html')

@app.route('/data/save/delete')
def data_save_delete():
    db = DB.getDB()
    id = request.values.get('id')
    name = request.values.get('name')
    age = request.values.get('age')
    sql = ""

    if id == "" and name == "" and age == "":
        return redirect('/data/delete')
    elif len(id) == 0:
        if len(name) != 0 and len(age) != 0:
            sql = "delete from student where name='%s' and age='%s'" % (name, age)
        elif len(name) != 0 and len(age) == 0:
            sql = "delete from student where name='%s'" % name
        elif len(name) == 0 and len(age) != 0:
            sql = "delete from student where age='%s'" % age
    elif len(name) == 0:
        if len(id) != 0 and len(age) != 0:
            sql = "delete from student where id='%s' and age='%s'" % (id, age)
        elif len(id) == 0 and len(age) != 0:
            sql = "delete from student where age='%s'" % age
        elif len(id) != 0 and len(age) == 0:
            sql = "delete from student where id='%s'" % id
    elif len(age) == 0:
        if len(id) != 0 and len(name) != 0:
            sql = "delete from student where id='%s' and name='%s'" % (id, name)
        elif len(id) != 0 and len(name) == 0:
            sql = "delete from student where id='%s'" % id
        elif len(id) == 0 and len(name) != 0:
            sql = "delete from student where name='%s'" % name

    db.query(sql)
    return redirect('/data/show')

@app.route('/data/cancel/delete')
def data_cancel_delete():
    return redirect('/data/show')

@app.route('/data/edit')
def data_edit():
    data = ("", "", "")
    return render_template('update.html', fs=data)

@app.route('/data/update/edit')
def data_update_edit():
    db = DB.getDB()
    id = request.values.get('id')
    if len(id) == 0:
        return redirect('/data/edit')
    else:
        sql = "select * from student where id='%s'" % id
        data = db.queryOne(sql)
        return render_template('update.html', fs=data)

@app.route('/data/update/cancel')
def data_update_cancel():
    return redirect('/data/show')

@app.route('/data/update/save')
def data_update_save():
    db = DB.getDB()
    id = request.values.get('id')
    name = request.values.get('name')
    age = request.values.get('age')

    if len(name) == 0 or len(age) == 0:
        return redirect('/data/show')
    else:
        sql = "update student set name='%s', age='%s' where id='%s'" % (name, age, id)
        db.query(sql)
        return redirect('/data/show')

if __name__ == '__main__':
    app.run(debug=True)
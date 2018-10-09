#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import DB

app = Flask(__name__)
app.config["SECRET_KEY"] = 'TEST'

@app.route('/')
@app.route('/list')
def data_list():
    db = DB.getDB()
    n, rows =db.query('select * from student')
    return render_template('/list.html', data=rows)

@app.route('/edit/<id>')
def data_edit(id):
    db = DB.getDB()
    fs = (id , "", "")
    if int(id) != 0:
        fs = db.queryOne('select * from student where id=%s' % id)
    return render_template('/edit.html', fs=fs)

@app.route('/save')
def data_save():
    db = DB.getDB()
    id = request.values.get('id')
    name = request.values.get('name')
    age = request.values.get('age')

    if int(id) != 0:
        sql = "update student set name='%s', age='%s' where id='%s'" % (name, age, id)
    else:
        row = db.queryOne("select max(id) from student")
        maxid = int(row[0]) + 1
        sql = "insert into student values (%s, '%s', %s)" % (maxid, name, age)

    db.query(sql)
    return redirect('/list')

@app.route('/delraw/<id>')
def data_delete(id):
    db =DB.getDB()
    sql = "delete from student where id=%s" % id
    db.query(sql)
    return redirect('/list')



if __name__ == '__main__':
    app.run(debug=True)
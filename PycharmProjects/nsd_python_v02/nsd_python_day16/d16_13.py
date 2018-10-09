#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template
from flask import request
import db

app = Flask(__name__)

@app.route('/')
def show_data():
    database =db.getDB()
    n, rows = database.query('select * from student')
    return render_template('student.html', rows=rows)

@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/data/insert')
def data_insert():
    id = int(request.values.get('id'))
    name = request.values.get('name')
    age = int(request.values.get('age'))

    database = db.getDB()
    database.query('insert into student values (%d, "%s", %d)' % (id, name, age))

    n, rows = database.query('select * from student')
    return render_template('student.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import render_template
import DB

app = Flask(__name__)
app.config["SECRET_KEY"] = 'TEST'

@app.route('/')
@app.route('/show')
def data_show():
    db = DB.getDB()
    sql = "select * from student"
    n, rows = db.query(sql)
    return render_template('joint/main.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)
#!/bin/python
# coding=utf8

from flask import Flask, render_template, session, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"


@app.route('/')
def login():
    return render_template("login.html", msg="")


@app.route('/check')
def check():
    xm = request.values.get("xm")
    pwd = request.values.get("pwd")
    print login,pwd
    if xm == "tom" and pwd == "123":
        session["logined"] = True
        return "login Success! Welcome!"
    else:
        return render_template("login.html", msg="Name or Password is Wrong!! Try Again!")


@app.route('/showlist')
def showlist():
    if session["logined"] == True:
        return "This is showList Page!"
    else:
        return render_template("login.html", msg="You must login!")


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")

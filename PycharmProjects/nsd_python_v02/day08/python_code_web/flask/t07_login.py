#!/bin/python
# coding=utf8

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

from flask_login import login_required, LoginManager, UserMixin, login_user, logout_user

app.secret_key = 'test'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user_login'
login_manager.init_app(app)


class User(UserMixin):
    def get_id(self):
        return ""


@login_manager.user_loader
def load_user(user_id):
    return User()


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    next = request.values.get("next")
    if next == None:
        next = "/page2"
    return render_template("login.html", next=next)


@app.route("/user_logout")
def user_logout():
    logout_user()
    return "protected logout"


@app.route('/check', methods=['GET', 'POST'])
def check():
    xm = request.values.get("xm")
    pwd = request.values.get("pwd")
    if xm == "tom" and pwd == "123":
        login_user(User())
        next = request.values.get('next')
        return redirect(next)
    else:
        return redirect('/user_login')


# =================受保护的业务接口区======
@app.route("/page2")
@login_required
def page2():
    return "protected page2"


@app.route("/page3")
@login_required
def page3():
    return "protected page3"


if __name__ == '__main__':
    app.run(debug=True)

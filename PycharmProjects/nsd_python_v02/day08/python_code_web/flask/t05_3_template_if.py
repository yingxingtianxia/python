#!/bin/python
# coding=utf8

from flask import request, render_template
from flask import Flask

app = Flask(__name__)


# http://127.0.0.1:5000/test3_form.html

@app.route('/test')
def test():
    head = [u"编号", u"姓名", u"年龄"]
    rows = [
        [1, u"刘若英", 12], [2, u"刘德华", 42], [3, u"汪峰", 30], [4, u"周笔畅", 15],
    ]

    return render_template("template_if.html", head=head, rows=rows)


if __name__ == '__main__':
    app.run(debug=True)

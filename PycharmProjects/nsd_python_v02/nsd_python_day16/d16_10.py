#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from flask import session

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ABC'
@app.route('/<msg>')
def handler(msg):
    my = session.get('my')
    if isinstance(my, type([])):
        my.append(msg)
    else:
        my = []

    session['my'] = my
    return str(my)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
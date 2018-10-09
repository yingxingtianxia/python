#!/usr/bin/env python3

from flask import Flask



app = Flask(__name__)

@app.route('/img')
def hd():
    f = open('static/flunk.jpg', 'rb')
    bytes = f.read()
    f.close()
    return bytes, 200, {'Content-Type': "image/jpeg"}

if __name__ == '__main__':
    app.run()
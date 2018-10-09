#!/usr/bin/env python3
#--*--coding: utf8--*--
from flask import Flask
from nsd_python_v02.nsd_python_day18.mods.user import blue_user as user
from nsd_python_v02.nsd_python_day18.mods.product import blue_product as product
from nsd_python_v02.nsd_python_day18.mods.regist import blue_regist as regist
from nsd_python_v02.nsd_python_day18.mods.regist import blue_user_save as save
from nsd_python_v02.nsd_python_day18.mods.cart import blue_cart as cart

app = Flask(__name__, template_folder='views', static_url_path='/res', static_folder='res')
app.config['SECRET_KEY'] = 'TEST'

app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(regist)
app.register_blueprint(save)
app.register_blueprint(cart)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4500, threaded=True)


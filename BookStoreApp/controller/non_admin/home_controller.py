from flask import render_template

from BookStoreApp import app


@app.route('/')
def home():
    return render_template('/non_admin/home.html')


@app.route('/gio-hang')
def cart():
    return render_template('/non_admin/cart.html')



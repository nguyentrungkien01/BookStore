from flask import render_template

from BookStoreApp import app


@app.route('/')
def home():
    return render_template('/non_admin/home.html')


@app.route('/gio-hang')
def cart():
    return render_template('/non_admin/cart.html')


@app.route('/tai-khoan')
def account():
    return render_template('/non_admin/account.html')


@app.route('/chi-tiet-sach')
def book_detail():
    return render_template('/non_admin/book-detail.html')


@app.route('/sach-kinh-te')
def category():
    return render_template('/non_admin/economy-book.html')
from flask import render_template, redirect
from flask_login import logout_user

from BookStoreApp import app
from BookStoreApp.service.non_admin.category_service import get_all_category, \
    get_newest_book, get_recommend_book, get_top_selling_book, get_coming_book


@app.context_processor
def common_processor():
    return {
        'common_categories': get_all_category()
    }


@app.route('/')
def home():
    newest_books = get_newest_book()
    recommend_books = get_recommend_book()
    top_selling_books = get_top_selling_book()
    coming_books = get_coming_book()
    return render_template('/non_admin/home.html',
                           newest_books=newest_books,
                           recommend_books=recommend_books,
                           top_selling_books=top_selling_books,
                           coming_books=coming_books)


@app.route('/tai-khoan')
def account():
    return render_template('/non_admin/account.html')


@app.route('/bao-tri')
def maintain():
    return render_template('/non_admin/maintain.html')


@app.route('/client/api/log-out')
def log_out_client():
    logout_user()
    return redirect('/')

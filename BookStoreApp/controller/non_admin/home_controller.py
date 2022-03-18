from flask import render_template, redirect
from flask_login import logout_user

from BookStoreApp import app
from BookStoreApp.service.non_admin.category_service import get_all_category, \
    get_newest_book, get_recommend_book, get_all_attachment


@app.context_processor
def common_processor():
    return {
        'common_categories': get_all_category()
    }


@app.route('/')
def home():
    newest_books = get_newest_book()
    recommend_books = get_recommend_book()
    attachments = get_all_attachment()
    return render_template('/non_admin/home.html',
                           newest_books=newest_books,
                           recommend_books=recommend_books,
                           attachments=attachments)


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

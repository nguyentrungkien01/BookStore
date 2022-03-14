import json

from flask import render_template, jsonify

from BookStoreApp import app, client
from BookStoreApp.controller.utils.utils_controller import encode_vigenere, decode_vigenere \
    , send_message_phone_number, send_mail


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


# @app.route('/test-vigenere')
# def test_vigenere():
#     data = {
#         'input_plain_text': 123456789,
#         'output_plain_text': decode_vigenere(encode_vigenere(123456789)),
#     }
#     return jsonify(data)

#
# @app.route('/test-phone-number')
# def test_phone_number():
#     send_message_phone_number('test message')
#     return jsonify({})


# @app.route('/test-mail')
# def test_mail():
#     send_mail('tai khoan gui',
#               'mat khau gui',
#               'tai khoan nhan',
#               'noi dung')
#     return jsonify({})

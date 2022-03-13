import json

from flask import render_template, jsonify

from BookStoreApp import app
from BookStoreApp.controller.utils.utils_controller import encode_vigenere, decode_vigenere


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


@app.route('/test-vigenere')
def test_vigenere():
    e = encode_vigenere(696969)
    data = {
        'len': len(e['cipher_text']),
        'output_plain_text': decode_vigenere(e['cipher_text'], int(e['secret_number']), int(e['division'])),
        'input_plain_text': 696969,
        'cipher_text': e['cipher_text']
    }
    return jsonify(data)


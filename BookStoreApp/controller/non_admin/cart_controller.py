import random

from flask import render_template, json, jsonify, request
from flask_login import current_user

from BookStoreApp import app
from BookStoreApp.service.non_admin.cart_service import get_book_in_not_paid_cart, \
    get_money_total, add_book_to_cart as abc, delete_book_in_cart as dbc, get_amount_book_in_cart, \
    update_ship_info as usi, pay_cart as pc
from BookStoreApp.controller.utils.utils_controller import decode_vigenere, send_message_phone_number


# Lấy view giỏ hàng
@app.route('/gio-hang')
def cart_detail():
    return render_template('/non_admin/cart.html')


# Lấy thông tin sách trong giỏ hàng
@app.route('/gio-hang/api/books')
def get_book_in_cart():
    account_id = current_user.account_id if current_user.is_authenticated else None
    books = get_book_in_not_paid_cart(account_id=account_id)
    return json.dumps(books)


# Lấy thông tin tổng tiền giỏ hàng
@app.route('/gio-hang/api/money_total')
def get_money_total_of_cart():
    account_id = current_user.account_id if current_user.is_authenticated else None
    money_total = get_money_total(account_id=account_id)
    return json.dumps(money_total)


# Thêm sách vào giỏ hàng
@app.route('/gio-hang/api/add-to-cart', methods=['post'])
def add_book_to_cart():
    book_id = request.json.get('book_id')
    amount = request.json.get('book_amount')
    if amount is None:
        amount = 1
    return jsonify(abc(book_id=decode_vigenere(book_id),
                       account_id=current_user.account_id,
                       amount=int(amount)))


# Giảm số lượng sách trong giỏ hàng
@app.route('/gio-hang/api/subtract-to-cart', methods=['post'])
def subtract_book_to_cart():
    book_id = request.json.get('book_id')
    return jsonify(abc(book_id=decode_vigenere(book_id),
                       account_id=current_user.account_id,
                       amount=-1))


# Xóa sách trong giỏ hàng
@app.route('/gio-hang/api/delete-to-cart', methods=['post'])
def delete_book_in_cart():
    book_id = request.json.get('book_id')
    return jsonify(dbc(book_id=decode_vigenere(book_id),
                       account_id=current_user.account_id))


# Lấy số lượng sách trong đơn hàng
@app.route('/gio-hang/api/amount-book')
def get_amount_book_in_cart_detail():
    account_id = current_user.account_id if current_user.is_authenticated else None
    return jsonify(get_amount_book_in_cart(account_id=account_id))


# Cập nhật thông tin ship hàng và gửi OTP
@app.route('/gio-hang/api/ship-info', methods=['post'])
def update_ship_info():
    account_id = current_user.account_id if current_user.is_authenticated else None
    customer_fullname = request.json.get('customer_fullname')
    customer_phone_number = request.json.get('customer_phone_number')
    customer_address = request.json.get('customer_address')
    customer_note = request.json.get('customer_note')
    cart_otp = str(random.randint(100000, 999999))
    usi(account_id=account_id,
        customer_fullname=customer_fullname,
        customer_phone_number=customer_phone_number,
        customer_address=customer_address,
        customer_note=customer_note,
        cart_otp=cart_otp)
    message = 'Mã OTP đơn hàng của bạn là: ' + cart_otp
    # send_message_phone_number(message=message)
    return jsonify({
        'cart_otp': 12345  #cart_otp
    })


# Thanh toán đơn hàng
@app.route('/gio-hang/api/pay')
def pay_cart():
    account_id = current_user.account_id if current_user.is_authenticated else None
    return jsonify(pc(account_id=account_id))

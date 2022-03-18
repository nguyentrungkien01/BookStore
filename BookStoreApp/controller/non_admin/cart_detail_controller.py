from flask import request, redirect, jsonify, json, render_template
from flask_login import login_user, current_user
from BookStoreApp import login, app
from BookStoreApp.service.non_admin.cart_detail_service import get_cart_detail as gcd

#  xuất thông tin tài khoản
@app.route('/client/api/cart-detail', methods=['POST'])
def cart_detail_account():
    id = current_user.account_id
    if id:
        return jsonify(gcd(id))
    return jsonify('error')


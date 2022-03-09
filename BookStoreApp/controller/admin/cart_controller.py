import json
from flask import request,  render_template, jsonify
from BookStoreApp import app
from BookStoreApp.service.admin.cart_service import get_info_user_in_cart as info_user, get_book_in_cart as gbic,\
    get_cart_model as gcm, get_info_user_data as giud, get_book as gb, get_list_total_money_by_cartId as gltmbc

# Lấy thông tin giỏ hàng của khách
@app.route("/admin/api/cart", methods=['post'])
def get_cart():
    data = json.loads(request.data)
    arr = data.get("arr")
    print(arr)
    if arr == 0:
        return jsonify(giud(info_user()), gb(gbic()), gltmbc(info_user()), gltmbc(info_user()))
    if arr == 1:
        print(sorted(gltmbc(info_user())))
        return jsonify(giud(info_user()), gb(gbic()), sorted(gltmbc(info_user())))
    else:
        print(sorted(gltmbc(info_user()),reverse=True))
        return jsonify(giud(info_user()), gb(gbic()), sorted(gltmbc(info_user()),reverse=True))



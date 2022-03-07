import json
from flask import request, redirect, render_template, jsonify
from BookStoreApp import app
from BookStoreApp.service.admin.cart_service import get_info_user_in_cart as info_user, get_book_in_cart as gbic

@app.route("/admin/api/cart", methods=['post'])
def get_cart():
    print("00000000000000000000000000000000000000000000000000-")
    print(gbic())
    print(info_user())
    # return render_template("/admin/cart.html", info_user=info_user(), list_book =gbic())
    return jsonify(len(gbic()))
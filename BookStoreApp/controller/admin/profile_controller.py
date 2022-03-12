import json
from flask import request, jsonify
from BookStoreApp import app
from BookStoreApp.service.admin.profile_service import get_info_user_by_account_id as giu,get_info

# Lấy thông tin giỏ hàng của khách
@app.route('/admin/profile/api/profile-info', methods=['post'])
def get_profile():
    data = json.loads(request.data)
    account_id = data.get('account_id')

    return jsonify(get_info(giu(account_id)))

import hashlib
from flask import request, redirect, jsonify, json, render_template
from flask_login import login_user, current_user
from BookStoreApp import login, app
from BookStoreApp.service.non_admin.account_info_service import get_account_info_by_id as gaibi, get_dictionary as gd,\
                            set_change_password as scp




#  xuất thông tin tài khoản
@app.route('/client/api/account-info', methods=['POST'])
def get_account_info():
    id = current_user.account_id
    if id:
        return jsonify(gd(gaibi(id)))

    return jsonify('error')


# thay đổi mật khẩu
@app.route('/client/api/change-password', methods=['POST'])
def set_change_password():
    data = json.loads(request.data)
    new_password = data.get('new_password')
    old_password = data.get('old_password')
    id = current_user.account_id
    print(current_user.password)
    if id and new_password and old_password:
        old_password_hashlib =  hashlib.md5(old_password.encode('utf8')).hexdigest()
        if current_user.password == old_password_hashlib:
            try:
                scp(new_password=new_password, account_id=id)
            except:
                return jsonify('error')
        else:
            return jsonify("wrong_password")
    return jsonify("successful")
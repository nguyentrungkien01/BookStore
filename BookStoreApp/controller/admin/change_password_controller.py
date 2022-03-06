import json
from flask import request,jsonify
from BookStoreApp import  app
from BookStoreApp.service.admin import account_service
from BookStoreApp.service.admin.account_service import get_account as ga, change_passwork as cp

# Đổi mật khẩu
@app.route("/admin/api/change_password", methods=['post'])
def change_passwork():
    if request.method.__eq__('POST'):
        result = True
        wrong_password = False
        data = json.loads(request.data)
        username = str(data.get("username"))
        old_password = str(data.get("old_password"))
        if username and old_password:
            if ga(username=username, password=old_password) == None:
                result= False
                wrong_password = True
            else:
                account = ga(username=username, password=old_password)
                new_password = str(data.get("new_password"))
                cp(new_password=new_password, account=account)
        else:
            result = False
    return jsonify(result=result, wrong_password= wrong_password)
import json
from flask_admin import expose
from flask_login import current_user

from BookStoreApp import  app
from flask import request,jsonify
from BookStoreApp.model_view.admin.base_view import BaseView
from BookStoreApp.controller.admin.change_password_controller import change_passwork as cp, get_account as ga

# Lớp tượng trưng cho trang chức năng đổi mật khẩu phía admin
class ChangePasswordView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/change_password.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return False


# Đổi mật khẩu
@app.route("/admin/api/change-password", methods=['post'])
def set_change_passwork():
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
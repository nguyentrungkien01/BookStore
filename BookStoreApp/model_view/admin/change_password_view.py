from flask_admin import expose
from flask_login import current_user

from BookStoreApp.model_view.admin.base_view import BaseView

# Lớp tượng trưng cho trang chức năng đổi mật khẩu phía admin
class ChangePasswordView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/change_password.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return False



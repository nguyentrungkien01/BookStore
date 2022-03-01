from flask_admin import expose
from flask_login import current_user

from BookStoreApp.model_view.admin.base_view import BaseView

# Lớp tượng trưng cho trang chức năng thông tin giỏ hàng khách hàng phía admin
class CartView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/cart.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return True
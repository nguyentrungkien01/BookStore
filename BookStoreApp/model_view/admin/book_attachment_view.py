from flask_admin import expose
from flask_login import current_user

from BookStoreApp.model_view.admin.base_view import BaseView


# Lớp tượng trưng cho trang chức năng chỉnh sửa bản xem trước của sách phía admin
class BookAttachmentView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/book_attachment.html')

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return True

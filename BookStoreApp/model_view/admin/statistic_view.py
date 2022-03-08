from flask_admin import expose
from flask_login import current_user

from BookStoreApp.model_view.admin.base_view import BaseView
from BookStoreApp.controller.utils.utils_controller import get_data_json_file as gdjf


# Lớp tượng trưng cho trang chức năng thống kê phía admin
class StatisticView(BaseView):
    @expose('/')
    def index(self):
        selections = gdjf('statistic_data.json')
        return self.render('/admin/statistic.html', selections=selections)

    def is_accessible(self):
        return current_user.is_authenticated

    def is_visible(self):
        return True

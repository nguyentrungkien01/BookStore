from flask_admin import AdminIndexView, expose
from flask_login import current_user


# Lớp tượng trưng cho trang home page
class HomeView(AdminIndexView):
    def is_visible(self):
        return not current_user.is_authenticated

    @expose('/')
    def index(self):
        return self.render('/admin/home_page.html')

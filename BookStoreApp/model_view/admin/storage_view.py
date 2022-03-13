from flask_admin.contrib.sqla.filters import FilterLike, FilterNotLike
from flask_admin.form import rules
from wtforms import validators
from wtforms.validators import DataRequired

from BookStoreApp import CategoryModel
from BookStoreApp.model.storage_model import StorageModel
from BookStoreApp.model_view.admin.base_model_view import BaseModelView


# Lớp này tượng trưng cho trang quản lý loại sách phía admin
class StorageView(BaseModelView):
    # Thuộc tính hiển thị
    column_sortable_list = ['storage_id',
                            'name']
    column_searchable_list = ['name']
    column_default_sort = 'storage_id'
    column_labels = dict(category_id='Mã kho chứa',
                         name='Tên kho chứa')

    # Lọc dữ liệu
    column_filters = (FilterLike(StorageModel.name, name='Tên kho chứa'),
                      FilterNotLike(StorageModel.name, name='Tên kho chứa'))

    # Form nhập thông tin
    form_rules = [
        rules.FieldSet(('name',), 'Thông tin kho chứa'),
        rules.FieldSet(('categories',), 'Thông tin khác có liên quan')
    ]
    form_args = dict(
        name=dict(validators=[DataRequired(), validators.Length(max=50)],
                  render_kw={
                      'placeholder': 'Tên kho chứa...'
                  })
    )

    # Danh sách các cột hiển thị
    def scaffold_list_columns(self):
        return ['storage_id',
                'name']

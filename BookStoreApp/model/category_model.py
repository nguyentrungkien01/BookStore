from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from BookStoreApp import db


# Lớp này tượng trưng cho bảng category dưới database
# Dùng chứa các thông tin của loại sách
class CategoryModel(db.Model):
    __tablename__ = 'category_model'
    __table_args__ = {'keep_existing': True}
    # Khóa chính
    category_id = Column(Integer, primary_key=True, autoincrement=True)

    # Thuộc tính
    name = Column(String(50), nullable=False, unique=True)

    # Khóa ngoại
    storage_id = Column(Integer, ForeignKey('storage_model.storage_id'))

    # Quan hệ
    books = relationship('BookModel', backref='category', lazy=True,
                         foreign_keys='[BookModel.category_id]')
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from BookStoreApp import db


# Lớp này tượng trưng cho bảng storage dưới database
# Dùng chứa các thông tin của loại sách
class StorageModel(db.Model):
    __tablename__ = 'storage_model'
    __table_args__ = {'keep_existing': True}
    # Khóa chính
    storage_id = Column(Integer, primary_key=True, autoincrement=True)

    # Thuộc tính
    name = Column(String(50), nullable=False, unique=True)

    # Quan hệ
    categories = relationship('CategoryModel', backref='storage', lazy=True,
                              foreign_keys='[CategoryModel.storage_id]')

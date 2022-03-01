from sqlalchemy import Column, Integer, String, ForeignKey

from BookStoreApp import db


# Lớp này tượng trưng cho bảng preview_model dưới database
# Chứa các thông tin bản xem trước của sách
class PreviewModel(db.Model):
    __tablename__ = 'preview_model'

    # Khóa chính
    preview_id = Column(Integer, primary_key=True, autoincrement=True)

    # Thuộc tính
    name = Column(String(100), nullable=False, unique=True)

    # Khóa ngoại
    book_id = Column(Integer, ForeignKey('book_model.book_id'))


from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

from BookStoreApp import db


# Lớp này tượng trưng cho bảng cart_model dưới database
# Chứa các thông tin của giỏ hàng
class CartModel(db.Model):
    __tablename__ = 'cart_model'

    # Khóa chính
    cart_id = Column(Integer, primary_key=True, autoincrement=True)

    # Thuộc tính
    is_paid = Column(Boolean, default=False)

    # Khóa ngoại
    customer_id = Column(Integer, ForeignKey('customer_model.account_id'))

    # Quan hệ
    books = relationship('BookModel', secondary='cart_detail_model',
                         backref=backref('carts', lazy=True), lazy=True)

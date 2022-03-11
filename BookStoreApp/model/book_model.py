from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.orm import relationship, backref

from BookStoreApp import db


# Lớp này tượng trưng cho bảng book_model dưới database
# Dùng để lưu thông tin của sách
class BookModel(db.Model):
    __tablename__ = 'book_model'
    __table_args__ = {'keep_existing': True}

    # Khóa chính
    book_id = Column(Integer, primary_key=True, autoincrement=True)

    # Thuộc tính
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL, default=0.0)
    image = Column(String(100), default='')
    like_amount = Column(Integer, default=0)
    is_free_ship = Column(Boolean, default=False)
    description = Column(Text, default='')

    # Khóa ngoại
    sale_id = Column(Integer, ForeignKey('sale_model.sale_id'))
    point_id = Column(Integer, ForeignKey('point_model.point_id'))
    manufacturer_id = Column(Integer, ForeignKey('manufacturer_model.manufacturer_id'))
    category_id = Column(Integer, ForeignKey('category_model.category_id'))
    attachment_id = Column(Integer, ForeignKey('attachment_model.attachment_id'))

    # Quan hệ
    previews = relationship('PreviewModel', backref='book', lazy=True,
                            foreign_keys='[PreviewModel.book_id]')

    def __str__(self):
        return '{}'.format(self.name)

    def set_image(self, url):
        self.image = url
from sqlalchemy import Column, Integer, ForeignKey

from BookStoreApp import db

# Biến này tượng trưng cho bảng book_attachment_model dưới database
# Chứa các thông tin đính kèm của sách
book_attachment_model = db.Table('book_attachment_model',
                                 Column('book_id', Integer,
                                        ForeignKey('book_model.book_id'), primary_key=True),
                                 Column('attach_book_id', Integer,
                                        ForeignKey('book_model.book_id'), primary_key=True),
                                 keep_existing=True)

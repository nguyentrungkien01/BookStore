import datetime

from BookStoreApp import db
from BookStoreApp.model.account_model import AccountModel
from BookStoreApp import CustomerModel,BookModel,CartModel, CategoryModel
from BookStoreApp import cart_detail_model

# Lấy tất cả dữ liệu trong giỏ hàng
def get_cart_model():
    return AccountModel.query.all()

def get_info_user_in_cart():
    query = db.session.query(CartModel.cart_id, AccountModel.username, AccountModel.first_name, AccountModel.last_name,
                             CustomerModel.phone_number).filter(CartModel.customer_id == CustomerModel.account_id)\
                            .filter(CustomerModel.account_id == AccountModel.account_id)
    return query.all()

def get_book_in_cart():
    query = db.session.query(CartModel.cart_id, BookModel.name, CategoryModel.name, BookModel.image,\
        BookModel.price * cart_detail_model.c.amount).filter(CartModel.cart_id == cart_detail_model.c.cart_id)\
        .filter(cart_detail_model.c.book_id==BookModel.book_id).filter(
        cart_detail_model.c.cart_id == CartModel.cart_id).filter(
        BookModel.category_id == CategoryModel.category_id)
    return query.all()




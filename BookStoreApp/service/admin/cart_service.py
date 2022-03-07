from BookStoreApp.repository.admin.cart_repository import get_book_in_cart as gbic,get_info_user_in_cart as info_user

# Lấy thông tin của khách hàng thông qua repository
def get_info_user_in_cart():
    return gbic()

# Lấy thông tin sách trong giỏ hàng thông qua repository
def get_book_in_cart():
    return info_user()
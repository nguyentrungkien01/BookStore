from BookStoreApp.repository.non_admin.cart_detail_repository import get_book_by_cart_id as gbbc,\
                    get_cart_detail as gcd, get_total_by_cart_id as gt
from BookStoreApp.controller.utils.utils_controller import encode_vigenere

# lấy thông tin từ tầng repository và chuyển sang dạng danh sách từ điển
def get_cart_detail(account_id = None, **kwargs):
    if account_id:
        account_data = []
        cart = gcd(account_id)
        for c in cart:
            books = ''
            status =''
            list_book = gbbc(c[0])
            if list_book:
                for lb in list_book:
                    books += ', ' + lb[0]
            if c[2] == True:
                status = 'Đã thanh toán'
            else:
                status = 'Chưa thanh toán'

            account_data.append({
                'id': encode_vigenere(c[0]),
                'date': c[1].strftime("%m/%d/%Y, %H:%M:%S"),
                'books': books[2:len(books)],
                'total': float(gt(c[0])),
                'status': status
            })

    return account_data


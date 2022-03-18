import math

from BookStoreApp.repository.non_admin.category_repository import get_all_category as gac, \
    get_book_in_category as gbc, get_top_selling_book_category as gtb, get_newest_book as gnb, \
    get_recommend_book as grb, get_all_attachment as gaa, get_category_by_id as gci
from BookStoreApp.controller.utils.utils_controller import encode_vigenere


# Lấy thông tin tất cả các category
def get_all_category(**kwargs):
    categories = gac()
    datas = []

    if categories is None or len(categories) == 0:
        return datas

    for category in categories:
        datas.append({
            'category_id': encode_vigenere(category[0]),
            'category_name': category[1]
        })
    return datas


# Lấy thông tin sách trong category cụ thể
def get_book_in_category(category_id=None, **kwargs):
    books = gbc(category_id=category_id)
    datas = []

    if books is None or len(books) == 0:
        return datas

    for book in books:
        book_sale_price = book[3] if book[5] is None else \
            math.floor(book[3] * book[5] / 100)
        datas.append({
            'book_id': encode_vigenere(int(book[0])),
            'book_name': book[1],
            'book_image': book[2],
            'book_price': '{:,.0f}'.format(book[3]),
            'book_author': book[4],
            'sale_percent': 0 if book[5] is None else book[5],
            'book_sale_price': '{:,.0f}'.format(book_sale_price)
        })

    return datas


# Lấy thông tin top 10 sách bán chạy nhất của trong category
def get_top_selling_book_category(category_id=None, **kwargs):
    books = gtb(category_id=category_id)
    datas = []

    if books is None or len(books) == 0:
        return datas

    for book in books:
        datas.append({
            'book_id': encode_vigenere(int(book[0])),
            'book_name': book[1],
            'book_image': book[2],
        })
    return datas


# Lấy thông tin tất cả sách mới trong tháng
def get_newest_book():
    newest_books = gnb()
    datas = []
    if newest_books is None or len(newest_books) == 0:
        return datas

    for book in newest_books:
        book_sale_price = book[3] if book[5] is None else \
            math.floor(book[3] * book[5] / 100)
        datas.append({
            'book_id': encode_vigenere(int(book[0])),
            'book_name': book[1],
            'book_image': book[2],
            'book_price': '{:,.0f}'.format(book[3]),
            'book_author': book[4],
            'sale_percent': 0 if book[5] is None else book[5],
            'book_sale_price': '{:,.0f}'.format(book_sale_price)
        })
    return datas


# Lấy thông tin sách đề xuất
def get_recommend_book():
    recommend_books = grb()
    datas = []
    if recommend_books is None or len(recommend_books) == 0:
        return datas

    for book in recommend_books:
        datas.append({
            'book_id': encode_vigenere(int(book[0])),
            'book_name': book[1],
            'book_image': book[2],
            'publish_date': book[3].strftime('%d/%m/%Y')
        })
    return datas


# Lấy tất cả các combo sách
def get_all_attachment():
    attachments = gaa()
    datas = []
    if attachments is None or len(attachments) == 0:
        return datas
    for attachment in attachments:
        datas.append({
            'attachment_id': encode_vigenere(int(attachment[0])),
            'attachment_name': attachment[1],
        })
    return datas


# Lấy thông tin loại sách dựa vào id
def get_category_name_by_id(category_id=None, **kwargs):
    category = gci(category_id=category_id)
    if category is None:
        return {}
    return {
        'category_name': category.name
    }

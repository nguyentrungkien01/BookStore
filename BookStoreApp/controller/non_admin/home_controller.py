from flask import render_template

from BookStoreApp import app
from BookStoreApp.service.non_admin.category_service import get_all_category, \
    get_newest_book, get_recommend_book, get_all_attachment


@app.context_processor
def common_processor():
    return {
        'common_categories': get_all_category()
    }


@app.route('/')
def home():
    newest_books = get_newest_book()
    recommend_books = get_recommend_book()
    attachments = get_all_attachment()
    return render_template('/non_admin/home.html',
                           newest_books=newest_books,
                           recommend_books=recommend_books,
                           attachments=attachments)


@app.route('/tai-khoan')
def account():
    return render_template('/non_admin/account.html')

# @app.route('/test-vigenere')
# def test_vigenere():
#     data = {
#         'input_plain_text': 1,
#         'output_plain_text': encode_vigenere(1),
#     }
#     return jsonify(data)

#
# @app.route('/test-phone-number')
# def test_phone_number():
#     send_message_phone_number('test message')
#     return jsonify({})


# @app.route('/test-mail')
# def test_mail():
#     send_mail('tai khoan gui',
#               'mat khau gui',
#               'tai khoan nhan',
#               'noi dung')
#     return jsonify({})

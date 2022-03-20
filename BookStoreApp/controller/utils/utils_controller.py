import json
import os
import random
import smtplib

from BookStoreApp import app, client


# Đọc dữ liệu từ file json
def get_data_json_file(filename):
    if filename:
        with open(os.path.join(app.root_path, 'data/{}'.format(filename)),
                  encoding='utf-8') as f:
            return json.load(f)


# Ghi dữ liệu xuống file json
def set_data_json_file(filename, data):
    if filename:
        with open(os.path.join(app.root_path, 'data/{}'.format(filename)), 'w',
                  encoding='utf-8') as f:
            return json.dump(data, f, ensure_ascii=True, indent=4)


# Mã hóa bằng thuật toán vigenere
def encode_vigenere(plain_text):
    # Lấy số nhỏ nhất và lớn nhất có 26 chữ số
    beg_num = '1'
    end_num = ''
    for x in range(1, 11):
        if len(beg_num) < 10:
            beg_num += '0'
        end_num += '9'

    # Chuyển đổi số đầu vào thành 1 số khác
    secret_number = random.randint(int(beg_num) - plain_text, int(end_num) - plain_text)
    secret_data = str(plain_text + secret_number)

    # tạo key
    first_key = ''
    second_key = ''
    key_source = [x for x in range(0, 10)]
    random.shuffle(key_source)
    for key in key_source:
        first_key += str(key)
    random.shuffle(key_source)
    for key in key_source:
        second_key += str(key)

    # Tạo bảng ánh xạ
    map_table = []
    map_pivot = [int(x) for x in first_key]
    for r in range(0, 10):
        map_table.append([map_pivot[c] for c in range(0, 10)])
        map_pivot.append(map_pivot.pop(0))

    # Ánh xạ và tiến hành mã hóa
    pivot = 0
    cipher_data = ''
    for sd in secret_data:
        cipher_data += str(map_table[first_key.index(second_key[pivot])][first_key.index(sd)])
        pivot += 1
        if pivot > 9:
            pivot = 0

    return '{first_key}{cipher_data}{second_key}{secret_number}' \
        .format(first_key=first_key,
                cipher_data=cipher_data,
                second_key=second_key,
                secret_number=secret_number)


# Giải mã bằng thuật toán Vigenere
def decode_vigenere(cipher_text):
    # Tách dữ liệu mã hóa
    first_key = cipher_text[:10]
    cipher_data = cipher_text[10:20]
    second_key = cipher_text[20:30]
    secret_number = int(cipher_text[30:])

    # Tạo bảng ánh xạ
    map_table = []
    map_pivot = [int(x) for x in first_key]
    for r in range(0, 10):
        map_table.append([map_pivot[c] for c in range(0, 10)])
        map_pivot.append(map_pivot.pop(0))

    # Ánh xạ và giải mã
    secret_data = ''
    pivot = 0
    for c in cipher_data:
        secret_data += first_key[map_table[first_key.index(second_key[pivot])].index(int(c))]
        pivot += 1
        if pivot > 9:
            pivot = 0
    plain_text = int(secret_data) - secret_number

    return plain_text


# Gửi tin nhắn
def send_message_phone_number(message):
    client.messages.create(
        from_='+17623025805',
        body=message,
        to='+84982482975'
    )


# Gửi mail
def send_mail(from_gmail_account, from_gmail_password, to_mail_account, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_gmail_account, from_gmail_password)
    server.sendmail(from_gmail_account,
                    to_mail_account,
                    message.encode('utf-8'))
    server.quit()

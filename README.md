# BookStore
Website quản lý mua bán sách online ứng dụng của môn `An Toàn Hệ Thống Thông Tin`

# Mô tả chung
- Mô hình: `MVC`
- Ngôn ngữ: `Python`, `Javascript (Jquery)`, `HTML`, `CSS`
- Framework, API, Library, Service: `Flask`, `SQLAlchemy`, `Bootstrap 4`, `Cloudinary`, `ChartJs`, `JsPDF`,  `Twillio`, `Province-Open`, `smtplib`,  `Sweet Alert`
- Database: `Mysql`
- Nền tảng deploy: `PythonAnywhere`
- IDE, Công cụ: `Pycharm`, `Vscode`, `MySQL Workbench`,`Git/GitHub`, `Trello`, `Diagrams.net`
- Khác: Thuật toán mã hóa demo (`Vigenere`-> Tự xây dựng, `md5`-> Sử dụng thư viện có sẵn)

# Chức năng (Có phân quyền người dùng)
- Quản trị viên
   + Đăng nhập
   + Đăng xuất
   + Xem thông tin cá nhân
   + Đổi mật khẩu tài khoản
   + Quản lý khách hàng: Xem, sắp xếp, tìm kiếm thông tin
   + Quản lý sách, loại sách, nhà xuất bản, bản xem trước, bản đính kèm sách, giảm giá, điểm, vai trò tài khoản: Thêm, sửa, xóa, xem, sắp xếp, tìm kiếm thông tin
   + Quản lý giỏ hàng của khách: Tìm kiếm, sắp xếp tăng, giảm theo giá trị đơn hàng
   + Thống kê doanh thu, tần suất bán sách theo tên sách: Thống kê theo tháng, quý, năm, giữa 2 tháng, giữa 2 quý, giữa 2 năm. Hiển thị dữ liệu thống kê ra biểu đồ và xuất ra pdf
   + Xem thông tin chung của website
   + Thống kê doanh thu ngày hiện tại so với ngày trước đó
   + Thống kê số lượng khách hàng trong tháng hiện tại
   + Thống kê top 10 loại sách bán chạy nhất
   + Báo cáo doanh thu, báo cáo tần suất bán sách: Báo cáo theo tháng, quý, năm. Xuất dữ liêu báo cáo ra pdf
- Khách hàng
   + Đăng nhập
   + Đăng xuất
   + Đăng ký tài khoản (Xác thực bằng gửi mã xác nhận qua email)
   + Đổi mật khẩu
   + Xem thông tin cá nhân
   + Xem thông tin các giỏ hàng đã thanh toán
   + Xem thông tin các các loại sách, sách mới, chi tiết loại sách ..
   + Xem chi tiết sách
   + Quản lý lịch sử thông tin những sách đã xem qua
   + Quản lý giỏ hàng cá nhân
   + Đặt hàng (Xác thực bằng gửi mã OTP đến điện thoại)
   
# Tóm tắt các ứng dụng bảo mật: 
   - Phân quyền người dùng
   - Mã hóa dữ liệu bằng thuật toán tự xây dựng
   - Xác thực bằng email
   - Xác thực bằng số điệ thoại
# Link video demo: 

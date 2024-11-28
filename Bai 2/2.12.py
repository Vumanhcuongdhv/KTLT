print("Vu Manh Cuong")
print("MSV: 235752021610030")
import re

# Danh sách để lưu trữ các mật khẩu hợp lệ
valid_passwords = []

# Nhập chuỗi mật khẩu từ bàn phím
items = [x.strip() for x in input("Nhập mật khẩu (cách nhau bằng dấu phẩy): ").split(',')]

# Kiểm tra từng mật khẩu
for password in items:
    # Kiểm tra độ dài
    if len(password) < 6 or len(password) > 12:
        continue
    
    # Kiểm tra các điều kiện khác
    if not re.search("[a-z]", password):  # Ít nhất 1 chữ cái thường
        continue
    if not re.search("[0-9]", password):  # Ít nhất 1 số
        continue
    if not re.search("[A-Z]", password):  # Ít nhất 1 chữ cái hoa
        continue
    if not re.search("[$#@]", password):  # Ít nhất 1 ký tự đặc biệt
        continue
    if re.search("\s", password):  # Không được chứa khoảng trắng
        continue
    
    # Nếu mật khẩu hợp lệ, thêm vào danh sách
    valid_passwords.append(password)

# In ra các mật khẩu hợp lệ, cách nhau bằng dấu phẩy
print("Mật khẩu hợp lệ:", ",".join(valid_passwords))

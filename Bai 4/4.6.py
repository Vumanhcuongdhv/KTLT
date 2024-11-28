print("Sinh vien: Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập tên người từ người dùng
full_name = input("Nhập tên người (họ và tên riêng): ")

# Tách họ và tên riêng
# Giả sử họ là phần đầu tiên và tên riêng là phần thứ hai
name_parts = full_name.split()

# Kiểm tra xem có đủ phần tử không
if len(name_parts) >= 2:
    last_name = name_parts[0]  # Họ
    first_name = name_parts[1]  # Tên riêng
else:
    last_name = full_name  # Nếu chỉ có một từ, coi đó là họ
    first_name = ""

# In ra họ và tên riêng
print("Họ:", last_name)
print("Tên riêng:", first_name)


print("Sinh vien: Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập danh sách các từ từ người dùng
input_list = input("Nhập danh sách các từ (cách nhau bởi dấu trống hoặc tab): ")

# Tách chuỗi thành danh sách, tự động xử lý cả dấu trống và tab
words = input_list.split()

# Đảo ngược danh sách
reversed_words = words[::-1]

# In ra các từ theo thứ tự ngược lại
print("Các từ theo thứ tự ngược lại là:", ' '.join(reversed_words))

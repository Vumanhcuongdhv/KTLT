print("Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập chuỗi ký tự từ bàn phím
input_string = input("Nhập vào một chuỗi ký tự: ")

# Tách chuỗi thành danh sách các từ
words = input_string.split()  # Mặc định tách theo khoảng trắng

# In ra danh sách các từ
print("Danh sách các từ trong chuỗi:")
print(words)

# Kết hợp lại các từ thành một chuỗi, sử dụng dấu phẩy và khoảng trắng
joined_string = ", ".join(words)

# In ra chuỗi đã kết hợp
print("Chuỗi đã kết hợp lại:")
print(joined_string)

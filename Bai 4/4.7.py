print("Sinh vien: Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập chuỗi từ người dùng
input_string = input("Nhập một chuỗi: ")

# Loại bỏ tất cả các chữ số
output_string = ''.join(char for char in input_string if not char.isdigit())

# In ra nội dung chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số:", output_string)


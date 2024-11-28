print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
# Nhập chuỗi các số nhị phân từ bàn phím
input_string = input("Nhập chuỗi các số nhị phân cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# Loại bỏ khoảng trắng (nếu có) xung quanh các số nhị phân
binary_numbers = [number.strip() for number in binary_numbers]

# In ra các giá trị đã nhập
print("Các số nhị phân đã nhập:")
for number in binary_numbers:
    print(number)

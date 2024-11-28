print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
# Nhập chuỗi các số từ bàn phím
input_string = input("Nhập các số cách nhau bằng dấu phẩy: ")

# Tách chuỗi thành danh sách các số
numbers = input_string.split(',')

# Chuyển đổi các số từ chuỗi sang số nguyên
numbers = [int(num.strip()) for num in numbers]

# Lọc các số lẻ
odd_numbers = [num for num in numbers if num % 2 != 0]

# Chuyển danh sách các số lẻ thành chuỗi cách nhau bởi dấu phẩy
result = ",".join(map(str, odd_numbers))

# In ra kết quả
print("Các số lẻ là:", result)

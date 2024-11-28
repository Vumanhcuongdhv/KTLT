print("Vu Manh Cuong")
print("MSV: 235752021610030")

# Nhập chuỗi ký tự từ bàn phím
input_string = input("Nhập vào một chuỗi ký tự: ")

# Tạo một dictionary để lưu trữ số lượng ký tự
char_count = {}

# Duyệt qua từng ký tự trong chuỗi
for char in input_string:
    if char in char_count:
        char_count[char] += 1  # Tăng số lượng nếu ký tự đã tồn tại
    else:
        char_count[char] = 1  # Khởi tạo số lượng nếu ký tự chưa tồn tại

# In ra kết quả
print("Số lượng ký tự trong chuỗi:")
print(char_count)

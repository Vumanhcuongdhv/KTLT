print("Sinh vien: Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập dãy các từ từ người dùng
input_string = input("Nhập một dãy các từ (cách nhau bởi dấu trống): ")

# Tách chuỗi thành danh sách các từ
words = input_string.split()

# Tìm độ dài của từ dài nhất
max_length = max(len(word) for word in words)

# Lọc ra các từ có độ dài bằng độ dài của từ dài nhất
longest_words = [word for word in words if len(word) == max_length]

# In ra các từ dài nhất
print("Các từ dài nhất là:", ', '.join(longest_words))


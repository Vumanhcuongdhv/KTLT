print("Sinh vien: Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập chuỗi S từ người dùng
S = input("Nhập chuỗi S: ")

# In từng ký tự của S trên một dòng, bỏ qua dấu cách và dấu tab, và chuyển thành chữ hoa
for char in S:
    if char not in [' ', '\t']:  # Kiểm tra xem ký tự có phải là dấu cách hoặc dấu tab không
        print(char.upper())  # Chuyển ký tự thành chữ hoa

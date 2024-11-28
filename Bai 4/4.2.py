print("Sinh vien: Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập chuỗi từ người dùng
S = input("Nhập chuỗi S: ")

# In từng ký tự không phải dấu space và dấu tab trên một dòng
for char in S:
    if char != ' ' and char != '\t':
        print(char)


print("Vu Manh Cuong")
print("MSV: 235752021610030")
# Yêu cầu người dùng nhập vào một số nguyên n
n = int(input("Nhập vào một số: "))

# Tạo một dictionary rỗng
d = dict()

# Sử dụng vòng lặp để đi qua các số từ 1 đến n
for i in range(1, n + 1):
    d[i] = i * i  # Thêm cặp (i, i*i) vào dictionary

# In ra dictionary
print(d)

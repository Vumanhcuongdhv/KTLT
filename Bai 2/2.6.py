print("Vu Manh Cuong")
print("MSV: 235752021610030")
# Tạo danh sách để lưu các số thỏa mãn điều kiện
result = []

# Duyệt qua các số trong khoảng từ 2000 đến 3200 (bao gồm cả 3200)
for i in range(2000, 3201):
    # Kiểm tra xem số có chia hết cho 7 và không phải bội số của 5
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))  # Lưu số vào danh sách dưới dạng chuỗi

# In các số ra màn hình, cách nhau bằng dấu phẩy
print(", ".join(result))

print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
ds = input("Nhập chuỗi: ").split()
print("List đã nhập:", ds)
# Tìm vị trí của phần tử 'abc' trong danh sách
if 'abc' in ds:  # Kiểm tra nếu 'abc' tồn tại trong danh sách
    print("Vị trí của chuỗi 'abc' là:", ds.index('abc'))
else:
    print("'abc' không có trong danh sách")

print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
ds = input("Nhập chuỗi: ").split()
print("List đã nhập:", ds)
# Bỏ phần tử '123' khỏi danh sách
if '123' in ds:  # Kiểm tra nếu '123' tồn tại trong danh sách
    ds.remove('123')
print("List sau khi bỏ '123':", ds)  # In toàn bộ danh sách

print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
ds = input("Nhập chuỗi: ").split()
print("List đã nhập:", ds)
if len(ds) > 2:  # Kiểm tra nếu list có đủ phần tử để cắt
    x = ds[1:-1]  # Cắt bỏ phần tử đầu và cuối
else:
    x = []  # Nếu không đủ phần tử, trả về list rỗng

print("List sau khi cắt:", x)

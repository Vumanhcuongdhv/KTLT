print("Vũ Mạnh Cường")
print("MSV:235752021610030")
# Hàm Sequential_Search thực hiện tìm kiếm tuyến tính trong danh sách
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)  # Trả về True và chỉ mục của phần tử tìm thấy
    return (False, -1)  # Trả về False nếu không tìm thấy phần tử
# Import hàm Sequential_Search từ module sequential_search
from sequential_search import Sequential_Search

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử của danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Tìm kiếm phần tử trong danh sách
found, index = Sequential_Search(dlist, item)

# Hiển thị kết quả tìm kiếm
if found:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {index}")
else:
    print(f"Phần tử {item} không được tìm thấy trong danh sách.")

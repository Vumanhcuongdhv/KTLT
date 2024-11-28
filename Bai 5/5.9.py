print("Vũ Mạnh Cường")
print("MSV:235752021610030")
# Hàm binary_search thực hiện tìm kiếm nhị phân trong một mảng đã sắp xếp
def binary_search(lst, value):
    lower_bound = 0
    upper_bound = len(lst) - 1

    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound) // 2  # Tính chỉ số trung điểm

        if lst[mid_point] == value:
            return True  # Phần tử được tìm thấy tại mid_point
        elif lst[mid_point] < value:
            lower_bound = mid_point + 1  # Tìm kiếm trong phần tử bên phải
        else:
            upper_bound = mid_point - 1  # Tìm kiếm trong phần tử bên trái

    return False  # Phần tử không tồn tại trong danh sách
# Import hàm binary_search từ module binary_search
from binary_search import binary_search

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử của danh sách
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    lst.append(value)

# Sắp xếp danh sách trước khi tìm kiếm
lst.sort()

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Tìm kiếm phần tử trong danh sách
found = binary_search(lst, value)

# Hiển thị kết quả tìm kiếm
if found:
    print(f"Phần tử {value} được tìm thấy trong danh sách.")
else:
    print(f"Phần tử {value} không tồn tại trong danh sách.")

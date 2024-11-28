print("Vũ Mạnh Cường")
print("MSV:235752021610030")
# Hàm sắp xếp danh sách theo thứ tự tăng dần
def sort_list(arr):
    return sorted(arr)

# Hàm tìm phần tử lớn nhất trong danh sách
def find_max(arr):
    return max(arr)
# Import các hàm từ module my_module
from my_module import sort_list, find_max

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các giá trị của danh sách
arr = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(value)

# Tìm phần tử nhỏ nhất và lớn nhất
min_value = min(arr)
max_value = find_max(arr)

# Tìm vị trí (index) của phần tử nhỏ nhất và lớn nhất
min_index = arr.index(min_value)
max_index = arr.index(max_value)

# Sắp xếp danh sách
sorted_arr = sort_list(arr)

# In kết quả
print(f"Danh sách ban đầu: {arr}")
print(f"Danh sách sau khi sắp xếp: {sorted_arr}")
print(f"Phần tử nhỏ nhất: {min_value} tại vị trí {min_index}")
print(f"Phần tử lớn nhất: {max_value} tại vị trí {max_index}")


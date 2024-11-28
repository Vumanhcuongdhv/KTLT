print("Vũ Mạnh Cường")
print("MSV:235752021610030")
# Hàm bubbleSort sắp xếp mảng theo thuật toán sắp xếp nổi bọt (Bubble Sort)
def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n):
        swapped = False  # Biến kiểm tra xem có trao đổi phần tử nào trong vòng lặp không
        for j in range(n - 1 - i):  # Chạy qua các phần tử chưa được sắp xếp
            if nlist[j] > nlist[j + 1]:  # So sánh các phần tử cạnh nhau
                # Hoán đổi các phần tử nếu chúng không theo thứ tự
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # Nếu không có phần tử nào bị hoán đổi trong vòng lặp, mảng đã được sắp xếp
        if not swapped:
            break
    return nlist
# Import hàm bubbleSort từ module bubble_sort
from bubble_sort import bubbleSort

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử của danh sách
nlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    nlist.append(value)

# Sắp xếp danh sách bằng thuật toán Bubble Sort
sorted_list = bubbleSort(nlist)

# In danh sách đã sắp xếp
print("Danh sách đã sắp xếp:", sorted_list)

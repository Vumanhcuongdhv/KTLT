print("Vũ Mạnh Cường")
print("MSV:235752021610030")
import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])

# Sử dụng lexsort để sắp xếp theo chiều cao trước, sau đó theo ID sinh viên
# Chúng ta cần truyền vào danh sách các mảng theo thứ tự sắp xếp: chiều cao trước, ID sau.
sorted_indices = np.lexsort((student_id, student_height))

# In chỉ số mô tả thứ tự sắp xếp
print("Chỉ số:")
print(sorted_indices)

# In dữ liệu đã sắp xếp theo thứ tự chỉ số
print("\nDữ liệu sắp xếp:")
for index in sorted_indices:
    print(student_id[index], student_height[index])

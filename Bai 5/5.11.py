print("Vũ Mạnh Cường")
print("MSV:235752021610030")
import numpy as np

# Định nghĩa kiểu dữ liệu của mảng có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu về sinh viên: tên, lớp, chiều cao
students_details = [('James', 5, 48.5), 
                    ('Nail', 6, 52.5), 
                    ('Paul', 5, 42.1), 
                    ('Pit', 5, 40.11)]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

# In mảng ban đầu
print("Original array:")
print(students)

# Sắp xếp mảng theo lớp và chiều cao nếu lớp giống nhau
sorted_students = np.sort(students, order=['class', 'height'])

# In mảng đã sắp xếp
print("\nSorted array:")
print(sorted_students)

print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def pascal_triangle(n):
    """Hàm in ra n dòng đầu tiên của tam giác Pascal."""
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Tạo dòng mới với tất cả các phần tử là 1
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  # Tính giá trị ở giữa
        triangle.append(row)

    return triangle

# Nhập số n từ bàn phím
n = int(input("Nhập số nguyên dương n: "))

# Lấy tam giác Pascal và in ra
pascal_rows = pascal_triangle(n)

print("Tam giác Pascal với", n, "dòng:")
for row in pascal_rows:
    print(" ".join(map(str, row)))

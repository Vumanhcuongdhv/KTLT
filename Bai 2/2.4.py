print("Vu Manh Cuong")
print("MSV: 235752021610030")
# Nhập khoảng a và b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Lặp qua từng số trong khoảng a đến b
for i in range(a, b + 1):
    # Tính số nghịch đảo và in ra kết quả dạng thập phân
    reciprocal = 1 / i
    print(f"Reciprocal of {i} is {reciprocal:.6f}")

print("Vu Manh Cuong")
print("MSV: 235752021610030")
# Khởi tạo biến
a, b = 0, 1
fibonacci_numbers = []
even_sum = 0

# Tính toán dãy số Fibonacci
while b < 4000000:
    fibonacci_numbers.append(b)  # Thêm số Fibonacci vào danh sách
    if b % 2 == 0:  # Kiểm tra xem số có chẵn không
        even_sum += b  # Cộng vào tổng nếu là số chẵn
    a, b = b, a + b  # Cập nhật giá trị a và b

# In ra dãy số Fibonacci
print("Dãy số Fibonacci nhỏ hơn 4.000.000:")
print(fibonacci_numbers)

# In ra tổng các số chẵn
print("Tổng các số chẵn trong dãy Fibonacci:", even_sum)

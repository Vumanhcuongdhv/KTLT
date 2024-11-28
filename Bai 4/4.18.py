print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def fibonacci_less_than_n(n):
    """Hàm tạo danh sách các số Fibonacci nhỏ hơn n."""
    fib_list = []
    a, b = 0, 1
    
    while a < n:
        fib_list.append(a)
        a, b = b, a + b  # Tính số Fibonacci tiếp theo

    return fib_list

# Nhập số nguyên n từ bàn phím
n = int(input("Nhập số nguyên dương n: "))

# Lấy danh sách các số Fibonacci nhỏ hơn n
fibonacci_numbers = fibonacci_less_than_n(n)

# In ra danh sách
print("Danh sách các số Fibonacci nhỏ hơn", n, "là:", fibonacci_numbers)

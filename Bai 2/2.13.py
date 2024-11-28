print("Vu Manh Cuong")
print("MSV: 235752021610030")
import math

# Nhập các hệ số a, b, c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra hệ số a
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        # Phương trình bậc nhất bx + c = 0
        x = -c / b
        print(f"Phương trình bậc nhất có nghiệm: x = {x}")
else:
    # Tính discriminant (delta)
    delta = b**2 - 4*a*c
    
    # Phân tích các trường hợp của delta
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm duy nhất: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")

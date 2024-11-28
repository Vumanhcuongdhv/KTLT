print("Vũ Mạnh Cường")
print("MSV 235752021610030")
# Hàm cộng
def add(x, y):
    return x + y

# Hàm trừ
def subtract(x, y):
    return x - y

# Hàm nhân
def multiply(x, y):
    return x * y

# Hàm chia
def divide(x, y):
    if y != 0:  # Kiểm tra nếu mẫu số khác 0
        return x / y
    else:
        return "Không thể chia cho 0!"

# Hiển thị lựa chọn
print("Chọn phép toán.")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")

# Lấy input từ người dùng
choice = input("Nhập lựa chọn (1/2/3/4): ")
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

# Thực hiện phép toán dựa trên lựa chọn
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Lựa chọn không hợp lệ")

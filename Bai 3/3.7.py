print("Vũ Mạnh Cường")
print("MSV 235752021610030")
def checkValue(n):
    if n % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")

# Nhập giá trị từ người dùng
try:
    user_input = int(input("Vui lòng nhập một số nguyên: "))
    checkValue(user_input)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")

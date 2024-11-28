print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def check_divisibility_by_5(binary_numbers):
    """Hàm kiểm tra các số nhị phân có chia hết cho 5 không."""
    divisible_by_5 = []

    for binary in binary_numbers:
        # Chuyển đổi số nhị phân sang thập phân
        decimal = int(binary, 2)
        if decimal % 5 == 0:
            divisible_by_5.append(binary)

    return divisible_by_5

# Nhập chuỗi các số nhị phân từ bàn phím
input_string = input("Nhập chuỗi các số nhị phân 4 chữ số cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# Kiểm tra và lấy các số chia hết cho 5
result = check_divisibility_by_5(binary_numbers)

# In ra kết quả
if result:
    print("Các số chia hết cho 5 là:", ",".join(result))
else:
    print("Không có số nào chia hết cho 5.")

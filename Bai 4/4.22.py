print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def is_all_digits_even(num):
    """Hàm kiểm tra xem tất cả các chữ số của số có phải là số chẵn không."""
    return all(int(digit) % 2 == 0 for digit in str(num))

# Tìm các số trong đoạn từ 1000 đến 3000
even_digit_numbers = [num for num in range(1000, 3001) if is_all_digits_even(num)]

# Chuyển danh sách thành chuỗi cách nhau bởi dấu phẩy
result = ",".join(map(str, even_digit_numbers))

# In ra kết quả
print("Các số có tất cả chữ số là số chẵn trong đoạn 1000 đến 3000 là:")
print(result)

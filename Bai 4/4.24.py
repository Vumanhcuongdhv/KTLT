print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def count_upper_and_lower(sentence):
    """Hàm đếm số chữ hoa và chữ thường trong câu."""
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():  # Kiểm tra xem ký tự có phải là chữ hoa không
            upper_count += 1
        elif char.islower():  # Kiểm tra xem ký tự có phải là chữ thường không
            lower_count += 1

    return upper_count, lower_count

# Nhập câu từ bàn phím
input_sentence = input("Nhập một câu: ")

# Đếm số chữ hoa và chữ thường
uppercase, lowercase = count_upper_and_lower(input_sentence)

# In ra kết quả
print(f"Chữ hoa: {uppercase}")
print(f"Chữ thường: {lowercase}")

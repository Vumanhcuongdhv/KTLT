print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def count_letters_and_digits(sentence):
    """Hàm đếm số chữ cái và chữ số trong câu."""
    letter_count = 0
    digit_count = 0

    for char in sentence:
        if char.isalpha():  # Kiểm tra xem ký tự có phải là chữ cái không
            letter_count += 1
        elif char.isdigit():  # Kiểm tra xem ký tự có phải là chữ số không
            digit_count += 1

    return letter_count, digit_count

# Nhập câu từ bàn phím
input_sentence = input("Nhập một câu: ")

# Đếm số chữ cái và chữ số
letters, digits = count_letters_and_digits(input_sentence)

# In ra kết quả
print(f"Số chữ cái là: {letters}")
print(f"Số chữ số là: {digits}")

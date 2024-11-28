print("Vũ Mạnh Cường")
print("MSV:235752021610030")
class RomanToInt:
    # Bảng tra cứu các ký tự La Mã và giá trị tương ứng
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def __init__(self, roman):
        self.roman = roman

    def convert(self):
        total = 0
        prev_value = 0

        # Duyệt qua từng ký tự của chuỗi La Mã từ phải sang trái
        for char in reversed(self.roman):
            current_value = self.roman_map[char]
            
            # Nếu giá trị hiện tại nhỏ hơn giá trị trước đó, trừ nó đi (quy tắc La Mã)
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Cập nhật giá trị trước đó
            prev_value = current_value

        return total

# Chuyển đổi số La Mã "XLII" (42)
roman_numeral = "XLII"
converter = RomanToInt(roman_numeral)
print(f"Số La Mã {roman_numeral} chuyển thành số nguyên là: {converter.convert()}")

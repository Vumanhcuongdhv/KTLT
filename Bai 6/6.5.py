print("Vũ Mạnh Cường")
print("MSV:235752021610030")
class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        # Tách chuỗi thành danh sách các từ
        words = self.text.split()
        
        # Đảo ngược danh sách các từ
        words.reverse()
        
        # Ghép các từ lại thành chuỗi sau khi đảo ngược
        reversed_text = ' '.join(words)
        
        return reversed_text

# Dữ liệu vào
input_text = "hello .py"

# Tạo đối tượng ReverseWords
reverse_words = ReverseWords(input_text)

# In ra dữ liệu vào
print(f"Dữ liệu vào: {input_text}")

# In ra kết quả sau khi đảo ngược
print(f"Dữ liệu sau khi đảo ngược: {reverse_words.reverse()}")

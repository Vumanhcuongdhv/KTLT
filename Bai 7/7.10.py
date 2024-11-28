print("Vũ Mạnh Cường")
print("235752021610030")
import re

def find_longest_words(text):
    # Tách các từ ra khỏi văn bản (chỉ lấy các chữ cái và chữ số, bỏ qua các dấu câu)
    words = re.findall(r'\b\w+\b', text)
    
    # Tìm độ dài của từ dài nhất
    max_length = max(len(word) for word in words)
    
    # Tìm những từ có độ dài bằng với độ dài của từ dài nhất
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words, max_length

def main():
    # Nhập văn bản (hoặc có thể thay bằng văn bản trong tệp)
    text = input("Nhập văn bản để tìm từ dài nhất: ")
    
    # Tìm những từ dài nhất trong văn bản
    longest_words, max_length = find_longest_words(text)
    
    # In kết quả
    print(f"Các từ dài nhất (có độ dài {max_length} ký tự):")
    for word in longest_words:
        print(word)

if __name__ == "__main__":
    main()

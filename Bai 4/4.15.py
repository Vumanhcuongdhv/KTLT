print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
# Nhập chuỗi từ bàn phím
input_string = input("Nhập chuỗi các từ tiếng Anh cách nhau bởi dấu cách: ")

# Tách chuỗi thành danh sách các từ
words = input_string.split()

# Sắp xếp danh sách theo thứ tự từ điển
sorted_words = sorted(words)

# In ra các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:")
for word in sorted_words:
    print(word)

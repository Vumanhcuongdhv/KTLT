print("Vũ Mạnh Cường")
print("MSV:235752021610030")
class StringManipulator:
    def __init__(self):
        self.user_string = ""  # Khởi tạo chuỗi rỗng

    # Phương thức nhận chuỗi từ người dùng
    def get_String(self):
        self.user_string = input("Nhập một chuỗi: ")  # Nhận chuỗi từ người dùng

    # Phương thức in chuỗi bằng chữ in hoa
    def print_String(self):
        print(self.user_string.upper())  # In chuỗi bằng chữ in hoa

# Tạo đối tượng của lớp StringManipulator
string_manipulator = StringManipulator()

# Nhận chuỗi từ người dùng
string_manipulator.get_String()

# In chuỗi đó bằng chữ in hoa
string_manipulator.print_String()

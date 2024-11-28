print("Vũ Mạnh Cường")
print("MSV:235752021610030")
class HinhChunhat(object):
    # Phương thức khởi tạo nhận chiều dài và chiều rộng
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    # Phương thức tính diện tích hình chữ nhật
    def area(self):
        return self.dai * self.rong

# Tạo đối tượng hinhChunhat với chiều dài 5 và chiều rộng 3
hinhChunhat = HinhChunhat(5, 3)

# In ra diện tích của hình chữ nhật
print(hinhChunhat.area())


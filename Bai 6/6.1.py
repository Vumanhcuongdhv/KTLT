print("Vũ Mạnh Cường")
print("MSV:235752021610030")
class Circle(object):
    # Phương thức khởi tạo, nhận bán kính r và gán cho thuộc tính radius
    def __init__(self, r):
        self.radius = r
    
    # Phương thức tính diện tích hình tròn
    def area(self):
        return self.radius ** 2 * 3.14

# Tạo đối tượng aCircle với bán kính 2
aCircle = Circle(2)

# In ra diện tích của hình tròn
print(aCircle.area())

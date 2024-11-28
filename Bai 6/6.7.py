print("Vũ Mạnh Cường")
print("MSV:235752021610030")
import math  # Để sử dụng giá trị pi chính xác

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Khởi tạo bán kính

    # Phương thức tính diện tích
    def area(self):
        return math.pi * self.radius ** 2  # Diện tích = π * r^2

    # Phương thức tính chu vi
    def circumference(self):
        return 2 * math.pi * self.radius  # Chu vi = 2 * π * r

# Tạo đối tượng Circle với bán kính 5
circle = Circle(5)

# In diện tích và chu vi của hình tròn
print(f"Diện tích hình tròn: {circle.area():.2f}")
print(f"Chu vi hình tròn: {circle.circumference():.2f}")

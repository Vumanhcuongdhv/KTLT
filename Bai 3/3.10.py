print("Vũ Mạnh Cường")
print("MSV 235752021610030")
import math

def Tinh(R):
    # Kiểm tra giá trị bán kính hợp lệ
    if R < 0:
        print("Bán kính không thể âm. Vui lòng nhập giá trị hợp lệ.")
        return
    
    # Tính chu vi và diện tích
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    
    # In kết quả
    print(f"Chu vi hình tròn: {chu_vi:.2f}")
    print(f"Diện tích hình tròn: {dien_tich:.2f}")

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính R: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")

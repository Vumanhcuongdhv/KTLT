
print("Vũ Mạnh Cường")
print("MSV 235752021610030")
import math

pos = [0, 0]  # Vị trí bắt đầu

while True:
    s = input("Nhập hướng di chuyển (hoặc nhấn Enter để kết thúc): ")
    if not s:  # Nếu không có input thì dừng vòng lặp
        break
    movement = s.split(" ")  # Tách chuỗi thành danh sách
    direction = movement[0]  # Lấy hướng di chuyển
    steps = int(movement[1])  # Lấy số bước đi

    # Cập nhật vị trí dựa trên hướng di chuyển
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        print("Hướng không hợp lệ!")

# Tính khoảng cách từ vị trí hiện tại về vị trí xuất phát
distance = math.sqrt(pos[1]**2 + pos[0]**2)

# In ra khoảng cách gần nhất với số nguyên
print(int(round(distance)))

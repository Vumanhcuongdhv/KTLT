print("Vũ Mạnh Cường")
print("MSV 235752021610030")
def benefit(t, n, k):
    # Tính số tiền nhận được sau k tháng
    # Công thức tính là: tiền = vốn * (1 + lãi suất) ^ số tháng
    return n * ((1 + t / 100) ** k)

# Nhập dữ liệu từ bàn phím
try:
    t = float(input("Nhập lãi suất tiết kiệm t (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu n: "))
    k = int(input("Nhập số tháng gửi k: "))
    
    # Tính số tiền nhận được
    total_amount = benefit(t, n, k)
    
    # In kết quả
    print(f"Số tiền nhận được sau {k} tháng là: {total_amount:.2f}")
except ValueError:
    print("Vui lòng nhập giá trị hợp lệ.")

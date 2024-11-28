print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
def process_transactions():
    """Hàm xử lý nhật ký giao dịch và tính số dư tài khoản."""
    balance = 0
    print("Nhập nhật ký giao dịch (D để gửi, W để rút, nhấn Enter để kết thúc):")
    
    while True:
        transaction = input()
        if transaction.strip() == "":  # Dừng nhập khi người dùng nhấn Enter
            break
        
        # Tách hành động và số tiền
        try:
            action, amount = transaction.split()
            amount = int(amount)  # Chuyển đổi số tiền thành kiểu số nguyên
            
            if action == 'D':  # Nếu là tiền gửi
                balance += amount
            elif action == 'W':  # Nếu là tiền rút
                balance -= amount
            else:
                print("Hành động không hợp lệ. Vui lòng sử dụng 'D' hoặc 'W'.")
        except ValueError:
            print("Định dạng nhập không hợp lệ. Vui lòng nhập lại.")
    
    return balance

# Tính số tiền thực
final_balance = process_transactions()

# In ra kết quả
print(f"Số tiền thực trong tài khoản là: {final_balance}")

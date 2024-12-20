print("Vũ Mạnh Cường")
print("MSV:235752021610030")
class ATM:
    def __init__(self, balance=1000):
        self.balance = balance  # Khởi tạo số dư ban đầu (mặc định là 1000)

    # Phương thức kiểm tra số dư
    def check_balance(self):
        print(f"Số dư tài khoản hiện tại: {self.balance} VND")

    # Phương thức nạp tiền
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount} VND vào tài khoản.")
        else:
            print("Số tiền nạp không hợp lệ!")

    # Phương thức rút tiền
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Đã rút {amount} VND từ tài khoản.")
        elif amount > self.balance:
            print("Số dư không đủ để rút tiền!")
        else:
            print("Số tiền rút không hợp lệ!")

# Hàm hiển thị menu và xử lý các giao dịch
def atm_menu():
    atm = ATM()  # Tạo đối tượng ATM với số dư ban đầu là 1000

    while True:
        print("\n--- Chào mừng đến với ATM ---")
        print("1. Kiểm tra số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Thoát")
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == "1":
            atm.check_balance()  # Kiểm tra số dư
        elif choice == "2":
            amount = float(input("Nhập số tiền cần nạp: "))
            atm.deposit(amount)  # Nạp tiền
        elif choice == "3":
            amount = float(input("Nhập số tiền cần rút: "))
            atm.withdraw(amount)  # Rút tiền
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ ATM. Tạm biệt!")
            break  # Thoát khỏi chương trình
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình ATM
atm_menu()

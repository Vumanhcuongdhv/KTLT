print("Vũ Mạnh Cường")
print("MSV:235752021610030")
class Nguoi(object):
    # Phương thức trả về giới tính mặc định (Unknown)
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    # Phương thức ghi đè để trả về "Nam"
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    # Phương thức ghi đè để trả về "Nữ"
    def getGender(self):
        return "Nữ"

# Tạo đối tượng của lớp Nam và Nu
aNam = Nam()
aNu = Nu()

# In ra giới tính của đối tượng aNam và aNu
print(aNam.getGender())  # Kết quả: "Nam"
print(aNu.getGender())   # Kết quả: "Nữ"

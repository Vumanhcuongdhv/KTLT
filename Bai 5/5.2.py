print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
import datetime as dt

# Định nghĩa định dạng thời gian
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển đổi chuỗi thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In các thông tin ngày tháng
print('Day: ' + str(t1.day))
print('Month: ' + str(t1.month))
print('Minute: ' + str(t1.minute))
print('Second: ' + str(t1.second))

# Định nghĩa thời gian hiện tại
t2 = dt.datetime.now()

# Tính hiệu giữa hai thời điểm
diff = t2 - t1

# In ra số ngày khác nhau
print('How many days difference? ' + str(diff.days))

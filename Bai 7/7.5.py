print("Vũ Mạnh Cường")
print("235752021610030")
def file_read(fname):
    # Mở tệp ở chế độ 'a' để nối thêm nội dung vào tệp
    with open(fname, "a") as myfile:
        # Nối văn bản vào tệp
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    
    # Mở tệp ở chế độ 'r' để đọc và hiển thị nội dung của tệp
    with open(fname, "r") as myfile:
        # Đọc và hiển thị toàn bộ nội dung tệp
        print(myfile.read())

# Gọi hàm để thực hiện chức năng
file_read('xyz.txt')



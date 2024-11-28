print("Vũ Mạnh Cường")
print("235752021610030")
from itertools import islice
def file_read_from_head(fname, nlines):
    with open(fname, 'r') as f:
        for line in islice(f, nlines):
            print(line, end='') # Gọi hàm với tệp 'test.txt' và số dòng cần đọc
file_read_from_head('test.txt', 2)


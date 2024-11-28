print("Vũ Mạnh Cường")
print("235752021610030")
def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file) 
filename = 'test.txt'
line_count = count_lines_in_file(filename)
print(f"Số dòng trong tệp '{filename}' là: {line_count}")

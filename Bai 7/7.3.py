print("Vũ Mạnh Cường")
print("235752021610030")
try:
    with open('D:/xinchao.txt', 'r') as file:  
        content = file.read() 
        print(content) 
except FileNotFoundError:
    print("Tệp không tồn tại. Hãy kiểm tra lại đường dẫn.")

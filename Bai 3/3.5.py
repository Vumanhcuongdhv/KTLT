print("Vũ Mạnh Cường")
print("MSV 235752021610030")
a = "Hello Guy!"

def say():
    global a
    a = "Vinh University"
    print(a)  # In ra biến a trong hàm

say()  # Gọi hàm say
print(a)  # In ra biến a sau khi gọi hàm

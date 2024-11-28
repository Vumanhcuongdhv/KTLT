print("Vũ Mạnh Cường")
print("MSV 235752021610030")
def get_sum(*num):
    tmp = 0
    # Duyệt qua các tham số
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)

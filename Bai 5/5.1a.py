print("Sinh viên: Vũ Mạnh Cường")
print("MSV:235752021610030")
# mymath.py
def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    total = 0.0
    for v in values:
        total += v
    return float(total) / nvals

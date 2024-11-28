print("Sinh viên: Vũ Mạnh Cường")
print("MSV: 235752021610030")
import mymath
# My script using the mymath module
import mymath  # Chú ý không có .py

values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(mymath.square(v))

print('Cubes:')
for v in values:
    print(mymath.cube(v))

print('Average: ' + str(mymath.average(values)))

# Lý thuyết:
a = 7
b = 8.5
c = "abc"
d1 = True
d2 = False
print(a)
print(type(b))

input("Input values: ")


# Baài tâập:
"""
    Hình tròn: nhập vào bán kính R
    Chu vi ?
    Diện tích ?
"""
from math import pi
R = float(input("Enter the radios of a circle: "))
print(R)
# print(type(R))

C = 2 * pi * R
print("Circumference of circle:", C)

A = pi * (R ** 2)
print("Area of circle:", A)


'''
    Nhập vào số nguyên n
    Tính và in ra tổng số đo các góc của đa giác n cạnh
'''
n = int(input("Enter the number: "))
if n < 3:
    print("The number is less than 3")
else:
    sum_angles = (n-2)


"""
    Nhập vào số nguyên t
    Hiện thị giờ tương ứng với định dạng:
    hh:mm:ss
"""
t = int(input("Enter the time: "))
h = (t // 3600) % 24
m = (t % 3600) // 60
s = (t % 3600) % 60
print(h, ":", m, ":", s)
"""
    Yêu cầu người dùng lần lượt nhập vào 2 số khác 0
    Tính và in ra màn hình tổng, hiệu, tích và thương của 2 số đó
"""

a = float(input("Enter the number a = "))
b = float(input("Enter the number b = "))

if a != 0 and b != 0:
    Sum = a + b
    Sub = a - b
    Mul = a * b
    Love = a / b
    print("Sum", Sum)
    print("Sub", Sub)
    print("Mul", Mul)
    print("Love", Love)
else:
    print("a,b > 0")
    a = float(input("ReEnter the number a = "))
    b = float(input("ReEnter the number b = "))

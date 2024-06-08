"""
    Yêu cầu người dùng nhập vào 3 số nguyên dương
    1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
    2. Nếu có thì kiểm tra tiếp xem đây là tam giác cân, tam giác đều,
    tam giác vuông hay tam giác thường
    3. Kiểm tra tiếp xem tam giác có góc tù hay không?
    4. Tính diện tích của tam giác
"""

a = int(input("Enter first edge a = "))
b = int(input("Enter 2nd edge b = "))
c = int(input("Enter 3rd edge c = "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b) or (a == c) or (c == b):
        print("...")

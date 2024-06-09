"""
    Yêu cầu người dùng nhập vào bán kính của hình tròn.
    Tính và hiển thị ra màn hình chu vi và diện tích của hình tròn tương ứng
"""

from math import pi

R = float(input("Enter the radius of the circle"))
# Perimeter:
C = 2 * pi * R
# Area:
A = pi * R ** 2
print("Perimeter:", C)
print("Area of circle:", A)

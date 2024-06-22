"""
    Yêu cầu người dùng nhập vào bán kính của hình tròn.
    Tính và hiển thị ra màn hình chu vi và diện tích của
    hình tròn tương ứng
"""

from math import pi

r = int(input('Enter radius of theb circle'))
# circumference:
c = 2 * pi * r
# area:
a = pi * r**2

print('circumference:', c)
print('area:', a)
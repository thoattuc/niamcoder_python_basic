"""
    Yêu cầu người dùng nhập vào 1 số nguyên n
    Tính và in ra tổng số đo các góc của đa giác đều n cạnh
"""

n = int(input('Enter a number: '))
if n >= 3:
    sum_angles = (n - 2) * 180
    print('Sum angles of polygons n edge:', sum_angles)
else:
    print('n >= 3')

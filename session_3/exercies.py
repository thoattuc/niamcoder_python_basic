"""
    Viết hàm tính và trả về khoảng cách giữa 2 điểm:
    - A(xa, ya, za)
    - B(xb, yb, zb)
    trong không gian 3 chiều
"""

from math import sqrt


# 1:
def cal_distance_1(a_coord, b_coord):
    xa, ya, za = a_coord
    xb, yb, zb = b_coord
    distance = sqrt((xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2)
    return distance


# 2:
def cal_distance_2(a_coord, b_coord):
    distance = 0
    for i in range(len(a_coord)):
        distance += (a_coord[i] - b_coord[i])**2
    return sqrt(distance)


# 3:
def cal_distance_3(a_coord, b_coord):
    distance = 0
    for i, j in zip(a_coord, b_coord):
        distance += (i - j)**2
    return sqrt(distance)


if __name__ == '__main__':
    A = (1, 2, 3)
    B = (3, 4, 5)
    print(cal_distance_1(A, B))
    print(cal_distance_2(A, B))
    print(cal_distance_3(A, B))

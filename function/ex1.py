"""
    Viết hàm tính và trả về khoảng cách giữa 2 điểm:
    - A(xa, ya, za)
    - B(xb, yb, zb)
    trong không gian 3 chiều
"""
from math import sqrt


def cal_distance(a_point, b_point):
    distance = 0
    for i, j in zip(a_point, b_point):
        distance += (i - j) ** 2
    return sqrt(distance)


if __name__ == '__main__':
    A = [1, 2, 3]
    B = [4, 5, 6]
    dis = cal_distance(A, B)
    print(dis)

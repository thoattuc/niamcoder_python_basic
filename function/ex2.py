"""
    Viết hàm nhận 3 số đầu vào, và trả về số lớn nất trong 3 số
    (Không dùng hàm max())
"""

# 1:


def get_max(a, b, c):
    max_number = 0
    for i in (a, b, c):
        if max_number <= i:
            max_number = i
    return max_number


if __name__ == '__main__':
    print(get_max(3,8,5))


# 2:
print(max(3, 8, 5))

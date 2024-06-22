"""
    Tìm số lớn nhất và nhỏ nhất trong dãy sau
"""

numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3, 5]
min_num = 0
max_num = 0
for i in range(0, len(numbers)):
    num = int(numbers[i])
    if num <= min_num:
        min_num = num
    elif num >= max_num:
        max_num = num
print(min_num, max_num)

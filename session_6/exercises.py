"""
    Cho list bao gồm các số bất kì
    Đếm xem số lần xuất hiện của mỗi số trong list đó
"""
numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]

# 1:
set_num = set(numbers)
list_num = list(set_num)
print(set_num)
for i in range(len(list_num)):
    count = 0
    for j in range(len(numbers)):
        if list_num[i] == numbers[j]:
            count += 1
    print(list_num[i], count)

# 2:
data = {}
for i in numbers:
    if i in data.keys():
        data[i] += 1
    else:
        data[i] = 1

for key, value in data.items():
    print("Number {} appears {} time(s)".format(key, value))


"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 chuỗi ký tự bất kỳ
    2. 1 số tự nhiên k bất kỳ
    Loại bỏ phần tử thứ k khỏi chuỗi và trả về chuỗi kết quả
"""

# string = "Today is a beautiful day!"
# k = 5

from string import punctuation

print(punctuation)

for i in punctuation:
    pass

"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    trả về số lần 1 ký tự lặp lại liên tiếp cho đến khi ký tự
    đó thay đổi
    Ví dụ, với input đầu vào là chuỗi "aabbbaccba"
    Output là [2, 3, 1, 2, 1, 1]
"""


def get_frequences(string):
    pass


text = "aabbbaccba"



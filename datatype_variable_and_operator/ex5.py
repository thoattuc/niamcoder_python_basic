"""
    Nhập vào số giây bất kỳ t (t là số nguyên dương bất kỳ)
    In ra màn hình thời gian tương ứng trong ngày dưới dạng
    hh : mm : ss
"""

t = int(input('Enter the times: '))
h = t // 3600
m = (t % 3600) // 60
s = (t % 60) % 60
print(h, ":", m, ":", s)

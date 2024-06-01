"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên bất kì
    Lấy ra chữ số hàng đơn vị theo 2 cách khác nhau
    rồi in ra màn hình
"""

n = int(input("Enter the number n = "))
if n % 10 == 0:
    print("unit digit = 0")
elif n % 10 != 0 and n % 10 < 10:
    m = n % 10
    print("unit digit = ", m)
else:
    p = n % 100
    print("unit digit = ", p)



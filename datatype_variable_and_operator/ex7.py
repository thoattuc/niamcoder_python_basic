"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên bất kì
    Lấy ra chữ số hàng đơn vị theo 2 cách khác nhau
    rồi in ra màn hình
"""

n = int(input('Enter the number: '))
# first:
digit_number_1 = n % 10
print("The unit digit number (1): ", digit_number_1)

# second:
n_str = str(n)
digit_number_2 = n_str[-1]
print("The unit digit number (2): ", digit_number_2)

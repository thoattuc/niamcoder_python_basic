"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên tương ứng
    với số đơn vị điện sử dụng của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền điện cho gia đình đó,
    với quy tắc sau:
    - 100 đơn vị đầu:                  Miễn phí
    - 100 đơn vị tiếp theo:            5$/đơn vị
    - Các đơn vị sau đó:               10$/đơn vị
"""

n = int(input('Enter the number of electric unit:'))
if n <= 100:
    cost = 0
elif (n > 100) and (n <= 200):
    cost = (n - 100) * 5
else:
    cost = (100 * 5) + ((n - 200) * 10)
print("Cost of use electric =", cost)

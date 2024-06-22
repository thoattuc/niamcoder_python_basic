"""
    Yêu cầu người dùng nhập vào 1 số dạng nhị phân (e.g. 1001)
    In ra giá trị dạng thập phân tương ứng của số đó
"""
# 1:
n = input("Enter a binary number: ")
binary_str = str(n)
decimal = 0
power = len(binary_str) - 1
for item in binary_str:
    if item == "1":
        decimal = decimal + 2 ** power
        power -= 1
print(decimal)

# 2:
binary_string = input("Enter a binary number: ")
decimal_number = int(binary_string, 2)
print(decimal_number)

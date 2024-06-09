"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    Tính n! theo 2 cách:
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
"""

# Use for-loop
n = int(input('[for-loop] Enter the number: '))
result = 1
for i in range(1, n + 1):
    result = result * i

print('The factorial of ', n, 'is', result)

# Use while-loop
a = int(input('[while-loop] Enter the number: '))
factorial = 1
count = 1
while count <= a:
    factorial *= count
    count += 1

print('The factorial of ', a, 'is', factorial)

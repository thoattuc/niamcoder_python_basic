"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    Tính n! theo 2 cách:
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
"""
# for:
n = int(input('Enter the number n = '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print('Factorial of', n,  '=', factorial)

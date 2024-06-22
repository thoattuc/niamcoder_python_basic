"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên lớn hơn 1
    1. Kiểm tra xem đó có phải là số nguyên tố hay không
    2. In ra màn hình tất cả các số nguyên tố nhỏ hơn hoặc bằng n
"""
# # 1:
# n = int(input("Enter the number n = "))
# for i in range(2, int(n**0.5) + 1):
#     # n se co 2 uoc: mot lon hon can bac hai cua n va mot nho hon can bac hai cua n
#     if n % i == 0:
#         print(n, "is not prime number")
#         break
#     else:
#         print(n, "is prime number")

# # 2:
# m = int(input("Enter a number m = "))
# for i in range(2, m):
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             print(i, "is not prime number")
#             break
#     else:
#         print(i, "is prime number")


"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra n số Fibonacci đầu tiên
    Định nghĩa dãy Fibonacci:
    Dãy Fibonacci bắt đầu với 2 số 1
    Các số sau được xác định bẳng tồng của 2 số ngay trước nó
    1 vài số Fibonacci đầu tiên trong dãy: 1, 1, 2, 3, 5, 8
"""
# # for:
# n = int(input("Enter the number n = "))
# a = 1
# b = 1
# for i in range(1, n+1):
#     new_n = a + b
#     print(a)
#     a = b
#     b = new_n

# while:
n = int(input("Enter the number n = "))
a = 1
b = 1
count = 1
while count < n+1:
    new_n = a + b
    print(a)
    a = b
    b = new_n
    count += 1

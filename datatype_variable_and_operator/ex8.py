"""
    Yêu cầu người dùng nhập vào 2 số bất kỳ.
    Viết chương trình để đổi giá trị 2 số đó với nhau theo 2 cách
"""
# first:
a = int(input('Enter the first number a = '))
b = int(input('Enter the second number b = '))
temp = a
a = b
b = temp
print('Wrapped value (1): a =', a, 'b =', b)

# second:
a, b = b, a
print('Wrapped value (2): a =', a, 'b =', b)

"""
    Nhập vào 2 số:
    - 1 số đại diện cho 1 năm
    - 1 số đại diện cho 1 tháng trong năm đó
    In ra màn hình số ngày của tháng đó
    Chú ý: Năm nhuận là năm thỏa mãn 1 trong 2 điều kiện sau:
    - Năm đó chia hết cho 4 nhưng không chia hết cho 100
    - Năm đó chia hết cho 400
"""

Y = int(input("Enter the year: "))
M = int(input("Enter the month: "))

if M in [1, 3, 5, 7, 8, 10, 12]:
    print("This month has: ", 31, "days")
elif M in [4, 6, 9, 11]:
    print("This month has: ", 30, "days")
elif M == 2:
    if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
        print("This month has: ", 29, "days")
    else:
        print("This month has: ", 28, "days")
else:
    print("Invalid month")

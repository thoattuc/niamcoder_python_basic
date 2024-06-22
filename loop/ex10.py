"""
    In ra các số có ít hơn 4 chữ số và chia hết cho cả 5 và 7
"""
arr = []
for i in range(1, 9999):
    if i % 5 == 0 and i % 7 == 0:
        arr.append(i)
print(arr)

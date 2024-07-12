# Khai bao list:
# data = []

data = [1, 2, "a", "b", "c"]
print(data[1])

data[0] = "first"
print(data)

value = ["x", "y", "z"]
data.append(value)
print(data)

print(data[5][1])

print(data[1:4:1])

# Them phan tu vao list:
data.insert(1, 10)
print(data)

data.append(12)
print(data)

data.extend([13, 14, 15])
print(data)

data += [100, 200]
print(data)

# Xoa phan tu khoi list:
data.pop(3)
print(data)

del data[3]
print(data)

del data[1:3]
print(data)

data.remove("c")
print(data)

# data.clear()

print(len(data))

# kiem tra su ton tai cua gia tri trong list
if 10 in data:
    print("true")
else:
    print("false")

# tim vi tri cua mot phan tu trong list
print(data.index(100))

# duyet cac phan tu cua list
for item in data:
    print(item)

# dao nguoc thu tu cua list
data.reverse()
print(data)

print(data[::-1])

# data.sort()
# print(data)
#
# sorted(data)
# print(data)

print(data.count(100))

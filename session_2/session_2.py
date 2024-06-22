# while loop:
number = 1
while number < 100:
    print(number)
    number *= 2

# for loop:
for i in range(10):
    print(i)

# break
for i in [12, 16, 17, 18, 19]:
    if i % 2 == 1:
        break
    print(i)
print("done")

# continue
for char in "Hiphop never dies":
    if char == "e":
        continue
    print(char)

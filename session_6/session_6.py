# Set:
data_1 = {"red", "green", "blue", 1, 3, 5, True}
print(data_1)
data_2 = set("string")
print(data_2)

# add:
data_2.add(5)
print(data_2)

# update:
data_1.update(data_2)
print(data_1)

# remove/discard/pop/clear:
data_1.remove("red")
print(data_1)

data_2.discard("green")
print(data_2)

data_1.pop()
print(data_1)

data_2.clear()
print(data_2)

# length:
print(len(data_1))

# duyet cac phan tu cua set:
for item in data_1:
    print(item)

# cac phep toan tap hop: union/intersection/difference/symmetric difference/
set_1 = {'red', 'green', 'blue'}
set_2 = {'yellow', 'red', 'orange'}

print(set_1 | set_2)
print(set_1.union(set_2))

print(set_1 & set_2)
print(set_1.intersection(set_2))

print(set_1 - set_2)
print(set_1.difference(set_2))
print(set_2 - set_1)
print(set_2.difference(set_1))

print(set_1 ^ set_2)
print(set_1.symmetric_difference(set_2))

# String:
data_str_1 = 'abc'
data_str_2 = "abcdefghijklmnopqrstuvwxyz"
data_str_3 = '''abcd'''

int_value = 1995
str_value = str(int_value)
print(str_value)
print(type(int_value))

print(data_str_1[1])
print(data_str_2[2:5])

print(data_str_3[::-1])

new_str = "P" + data_str_3[1:]
print(new_str)

string_1 = "hello" + "world"
print(string_1)

string_1 += "I start learning Python today"
print(string_1)

string_2 = "hello" "world" "!"
print(string_2)

string_2 = string_2 * 5
print(string_2)

print(len(string_2))

string_1 = string_1.replace("today", "every day!")
print(string_1)

print(string_1.lower())

print(string_2.upper())

print(string_1.capitalize())

print(string_2.title())

# escape characters: [\+character]
print("\'")
print("\\")
print("\"")
print("\n")
print("\t tab")

string_3 = "   Today is Sunday "
string_3 = string_3.strip()
print(string_3)

# Format String:
string_4 = input("Please, input info: ")
new_string = "....{}....".format(string_4)
print(new_string)

new_string = "....{1}....{0}....{2}....".format("hello", "world", "!")
print(new_string)

string_5 = "hello world !"
print(string_5.split())

new_string = string_3.split(" ")
print(new_string)

string_6 = " ".join(new_string)
print(string_6)

string_7 = "hello everyone!"
print(string_7.find("e"))   # index



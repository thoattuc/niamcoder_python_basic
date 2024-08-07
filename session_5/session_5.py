# Dictionary empty:
data_1 = {}
# Dictionary with key/value:
data_2 = {"name": "Niam", "age": "29", "job": "dev"}
# Dictionary with key is argument:
data_3 = dict(name="Niam", age="29", job="dev")
# Dictionary with a list of tuples:
data_4 = dict([("name", "Niam"), ("age", "29"), ("job", "dev")])
# Dictionary with a tuple of lists
data_5 = dict((["name", "Niam"], ["age", "29"], ["job", "dev"]))

A = {"day": "Sunday", "date": "080595", "Day": "Monday"}
print(A)

# Element access:
data = {"name": "Niam", "age": "29", "job": "dev"}
print(data["name"])
print(data.get("age"))  # tranh' bao' loi

# Update
data["gender"] = "Male"
data["age"] = 30
print(data)

# Delete:
removed_item = data.pop("gender")
print(data)

del data["age"]
print(data)

data.clear()
print(data)

# value, item,  key access:
data = {"name": "Niam", "age": "29", "job": "dev"}
print(data.values())  # dict:
print(data.keys())  # key
print(data.items())  # item

print(len(data))

# immutable:
a = 50
print(id(a))    # ...x

a = 60
print(id(a))    # ...y

# mutable:
list_number = [1, 2, 3, 5, 8]
print(id(list_number))  # ...z

list_number.append(13)
print(id(list_number))  # ...z





# Tuple packing:
data_tuples = ("red", "green", "yellow", "blue", "black")   # 5 values
a, b, c, d, e = data_tuples     # 5 variables

m, n = 3, 5
m, n = n, m
print(n, m)

print(data_tuples[0])   # access
print(data_tuples[1:3])     # slice
print(sorted(data_tuples))  # sort
print(data_tuples.count("yellow"))   # count value

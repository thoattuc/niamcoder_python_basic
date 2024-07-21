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

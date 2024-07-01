from math import e, pi, tau, inf, nan
from random import randint, random, choice, shuffle

print(e, pi, tau, inf, nan)

print(randint(3, 8))


def cal_sum_of_squares(n):
    result = 0
    for i in range(n + 1):
        result += i ** 2
    return result


if __name__ == '__main__':
    result_3 = cal_sum_of_squares(3)
    print(result_3)


def hello():
    print("Hello")


# position argument:
def func_position(name, job):
    print(name, job)


func_position("Nam", "dev")


# key argument:
def func_keyword(name, job):
    print(name, job)


func_keyword(job="dev", name="Nam")


# default argument:
def func_default(name, job="dev"):
    print(name, job)


func_default(name="Nam")


# nhieu gia tri tra ve:
def get_math_ops(a, b):
    return a + b, a - b, a * b, a / b


add, sub, mul, div = get_math_ops(5, 8)
print(add, sub, mul, div)


def func_docstring(a, b, c):
    """

    Parameters
    ----------
    a
    b
    c

    Returns
    -------

    """
    return


x = 5.5

y = int(x)
print(y)

z = str(x)
print(len(z))

# ham sap xep:
print(sorted([1, 2, 3, 4], reverse=True))

# ham lam tron so thap phan:
print(round(3.141592653589, 2))


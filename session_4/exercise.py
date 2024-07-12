# n = input("Enter the number: ")

# a = ["monday", "today"]
# print(sorted(a))

"""
    A.
    Viết hàm is_member() nhận 2 tham số đầu vào:
    1. 1 giá trị (số, chuỗi ký tự, bool, ...)
    2. 1 List chứa các giá trị bất kì
    Hàm kiểm tra xem giá trị có xuất hiện trong List hay không
    (Không dùng toán tử in)

    B.
    Viết hàm overlapping() nhận 2 tham số đầu vào là 2 List
    Hàm trả về danh sách các phần tử nằm ở cả 2 List
    Gợi ý: Sử dụng hàm is_member()
"""


def is_member(value, list_of_values):
    for i in list_of_values:
        if i == value:
            return "true"
        return "false"


def overlapping(list_1, list_2):
    new_list = []
    for i in range(len(list_1)):
        if is_member(list_1[i], list_2):
            new_list.append(list_1[i])
    return new_list


if __name__ == "__main__":
    print(is_member("monday", ["rose", 5, True, "monday", "tuesday", -5.5]))

    print(overlapping(["rose", 5, True], ["rose", 5, True, "monday", "tuesday", -5.5]))

"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    tách hàm ban đầu thành 2 nửa, được phân cách bởi
    phần tử có chỉ số là k (phần tử này sẽ thuộc về
    nửa thứ 2) rồi sau đó nối chúng lại sao cho nửa
    thứ 2 đứng ở trước nửa thứ nhất.
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 3
    Output:
        array = [4, 5, 1, 2, 3]
"""


# 1:
def split_array_1(array, k):
    length = len(array)
    result = [0]*len(arr)
    for index in range(length):
        result[index] = array[(index + k) % length]
    return result


# 2:
def split_array_2(array, k):
    k %= len(array)
    result = array[k:] + array[:k]
    return result


if __name__ == '__main__':
    arr = [11, 22, 33, 44, 55]
    x = 2
    print(split_array_1(arr, x))
    print(split_array_2(arr, x))

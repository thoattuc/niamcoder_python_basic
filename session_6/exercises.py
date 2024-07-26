"""
    Cho list bao gồm các số bất kì
    Đếm xem số lần xuất hiện của mỗi số trong list đó
"""
numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]

# 1:
set_num = set(numbers)
list_num = list(set_num)
print(set_num)
for i in range(len(list_num)):
    count = 0
    for j in range(len(numbers)):
        if list_num[i] == numbers[j]:
            count += 1
    print(list_num[i], count)

# 2:
data = {}
for i in numbers:
    if i in data.keys():
        data[i] += 1
    else:
        data[i] = 1

for key, value in data.items():
    print("Number {} appears {} time(s)".format(key, value))


"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n bất kì
    Tạo ra 1 dictionary với key lần lượt là các số từ
    0 đến n, và value là bình phương của key
"""
n = int(input("Enter a number: "))
result = {}
for i in range(n + 1):
    result[i] = i ** 2
print(result)


"""
    Viết chương trình kết hợp 2 dictionary vào làm 1.
    Nếu key xuất hiện ở cả 2 dictionary thì cộng 2 value
    tương ứng lại
"""
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

for key, value in dict2.items():
    if key in dict1.keys():
        dict1[key] += value
    else:
        dict1[key] = value
print(dict1)


"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 chuỗi ký tự bất kỳ
    2. 1 số tự nhiên k bất kỳ
    Loại bỏ phần tử thứ k khỏi chuỗi và trả về chuỗi kết quả
"""
string = "Today is a beautiful day!"
k = 5


def remove_char(string, k):
    if k < 0 or k >= len(string):
        return string
    result = string[:k] + string[k+1:]
    return result


print(remove_char(string, k))


"""
    Yêu cầu người dùng nhập vào 2 chuỗi ký tự bất kỳ.
    Kiểm tra xem chúng có phải anagrams (phép đảo chữ)
    của nhau không?
    Định nghĩa anagram: 2 từ là anagram của nhau nếu ta có thể
    thu được từ này bằng cách đổi vị trí các ký tự của từ kia
    Các ví dụ:
    "New York Times" và "monkeys write"
    "coronavirus" và "carnivorous"
    "a gentleman" = "elegant man"
    "silent" = "listen"
"""


def are_anagrams(str_1, str_2):
    str_1 = str_1.lower().replace(' ', '')
    str_2 = str_2.lower().replace(' ', '')
    return sorted(str_1) == sorted(str_2)


if __name__ == "__main__":
    str_1 = "New York Times"
    str_2 = "monkeys write"
    print(are_anagrams(str_1,str_2))


"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    hãy loại bỏ toàn bộ các dấu câu cũng như ký tự đặc biệt
    khỏi chuỗi ký tự đó và trả về kết quả
"""
from string import punctuation


def remove_punctuations(string):
    for p in punctuation:
        string = string.replace(p, "")
    return string


text = """
    Maya Angelo said, "If you don't like something, change it. 
    If you can't change it, change your attitude."
"""
print(remove_punctuations(text))


"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi ký tự bất kỳ,
    trả về số lần 1 ký tự lặp lại liên tiếp cho đến khi ký tự
    đó thay đổi
    Ví dụ, với input đầu vào là chuỗi "aabbbaccba"
    Output là [2, 3, 1, 2, 1, 1]
"""


def get_frequences(string):
    pass


text = "aabbbaccba"



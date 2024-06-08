"""
    Quy đổi điểm từ thang điểm 100 sang thang điểm chữ theo quy tắc:
        Điểm                             Quy đổi
        > 90                                A
        > 80 và <=90                        B
        > 60 và <= 80                       C
        <= 60                               D
"""
score = int(input('Enter a score'))
if score <= 60:
    grade = "D"
elif 60 < score <= 80:
    grade = "C"
elif 80 < score <= 90:
    grade = "B"
else:
    grade = "A"
print("Grade: ", grade)

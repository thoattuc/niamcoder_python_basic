"""
    Đếm số chẵn, lẻ, âm, dương trong dãy sau
"""
numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]
evens = 0
odds = 0
negatives = 0
positives = 0
for i in range(0, len(numbers)):
    print(numbers[i])
    if int(numbers[i]) % 2 == 0:
        evens += 1
        if int(numbers[i]) < 0:
            negatives += 1
        elif int(numbers[i]) >= 0:
            positives += 1
    elif int(numbers[i]) % 2 == 1:
        odds += 1
        if int(numbers[i]) < 0:
            negatives += 1
        elif int(numbers[i]) >= 0:
            positives += 1
print(evens, odds, negatives, positives)

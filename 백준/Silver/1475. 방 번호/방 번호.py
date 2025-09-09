from math import ceil

n = list(map(int, input()))
count = 0
number = [0] * 10
for i in n:
    number[i] += 1
number[6] = ceil((number[6] + number[9]) / 2)
number[9] = 0
print(max(number))

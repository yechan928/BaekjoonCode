numbers = []
for i in range (9):
    numbers.append(int(input()))
print(max(numbers))
print(numbers.index(max(numbers))+1)




# numbers=list(map(int,input().split()))
# max = numbers[0]
# for i in range(0,len(numbers)):
#     if numbers[i] > max : max =numbers[i]
# print(max)
# print(numbers.index(max)+1)
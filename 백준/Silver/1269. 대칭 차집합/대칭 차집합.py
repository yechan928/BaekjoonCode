import sys

a, b = map(int, sys.stdin.readline().split())
n = set(map(int, sys.stdin.readline().split()))
m = set(map(int, sys.stdin.readline().split()))
# 두 집항의 원소의 개수를 합치고 교집합 원소 개수 빼기
# count = 0
# for i in n:
#     for j in m:
#         if i == j:
#             count += 1

# print(a + b - (2 * count))


# set과 &연산자를 가지고 해보기
c = n & m
print(a + b - 2 * len(c))

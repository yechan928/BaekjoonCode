# 숫자의 합
import sys

n = int(sys.stdin.readline())
a = sys.stdin.readline().strip()
arr = list(map(int, a))

sum = 0
for i in arr:
    sum += i
print(sum)

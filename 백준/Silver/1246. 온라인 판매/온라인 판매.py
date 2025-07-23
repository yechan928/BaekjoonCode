import sys

n, m = map(int, sys.stdin.readline().split())

prices = [int(sys.stdin.readline()) for i in range(m)]
prices.sort()

max_ben = 0
best_pri = 0

for i, p in enumerate(prices):
    cnt = min(m - i, n)
    ben = p * cnt
    if ben > max_ben:
        max_ben = ben
        best_pri = p

print(best_pri, max_ben)

import sys
n, k = map(int, sys.stdin.readline().split())
coins=[int(sys.stdin.readline()) for _ in range(n) ]

count = 0
for i in range(n-1,-1,-1):
    count += k//coins[i]
    k = k%coins[i]

print(count)
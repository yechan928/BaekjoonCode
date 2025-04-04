import sys
t = int(sys.stdin.readline())
result=[]
for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    won = int(sys.stdin.readline())

    d=[0]*(won+1)
    d[0] = 1
    for coin in coins:
        for i in range(coin,won+1):
            d[i] += d[i-coin]
    result.append(d[won])

for i in result:
    print(i)
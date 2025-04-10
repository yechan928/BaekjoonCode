import sys
won = int(sys.stdin.readline())
coins = [2,5]
inf = float('inf')
dp = [inf]*(won+1)
dp[0]=0

count = 0
for coin in coins:
    for i in range(coin, won+1):
        dp[i] = min(dp[i],dp[i-coin]+1)

if dp[won]==inf:
    print(-1)
else:
    print(dp[won])
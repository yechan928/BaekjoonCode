n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

count = 0
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1 :
            continue
        step = arr[i][j]
        if i + step < n :
            dp[i+step][j] += dp[i][j]
        if j + step < n :
            dp[i][j+step] += dp[i][j]
print(dp[n-1][n-1])

import sys
s1 = list(' '+str(sys.stdin.readline().strip()))
s2 = list(' '+str(sys.stdin.readline().strip()))
dp = [[0]*(len(s1)) for _ in range(len(s2))]

for i in range(len(s2)):
    dp[i][0] = i
for j in range(len(s1)):
    dp[0][j] = j


for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s2[i]==s1[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
print(dp[-1][-1])